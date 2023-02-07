---
title: hadoop
date: 2023-02-07 15:34:42
tags: [学习, 大数据]
---

# Hadoop 为什么而生

Hadoop 的出生是为了解决`海量`的数据`计算和存储`而生

<!-- more -->

# Hadoop 的版本介绍

| 组件\版本 | V1.x      | V2.x      | V3.x      |
| --------- | --------- | --------- | --------- |
| 资源调度  | MapReduce | YARN      | YARN      |
| 计算组件  | MapReduce | MapReduce | MapReduce |
| 存储组件  | HDFS      | HDFS      | HDFS      |
| 辅助组件  | COMMON    | COMMON    | COMMON    |

# YARN

yarn 作为资源调度组件

# 安装 Hadoop 集群

## 准备工作

- 安装 epel-release

```shell
yum install -y epel-release
```

- 安装 net-tool(最小软件操作系统则需要安装)

```shell
yum install -y net-tool
```

- 安装 vim(最小软件操作系统则需要安装)

```shell
yum install -y vim
```

- 安装 rsync(最小软件操作系统则需要安装)

```shell
yum install -y rsync
```

- 关闭防火墙

```shell
systemctl stop firewalld
systemctl disable firewalld.service
```

- 虚拟机创建自定义用户(不用执行)

```shell
useradd bnyte
passwd ${username}
```

- 配置 bnyte 用户具有 root 权限(不用执行)

> 修改/etc/sudoers 文件，在%wheel 这行下面添加一行，如下所示：

```shell script
vim /etc/sudoers

## Allow root to run any commands anywhere
root ALL=(ALL) ALL
## Allows people in group wheel to run all commands
%wheel ALL=(ALL) AL

bnyte ALL=(ALL) NOPASSWD:ALL
# 注意：bnyte 这一行不要直接放到 root 行下面，因为所有用户都属于 wheel 组，你先
# 配置了 bnyte 具有免密功能，但是程序执行到%wheel 行时，该功能又被覆盖回需要
# 密码。所以 bnyte 要放到%wheel 这行下面。
```

> 为方便开发最好配置 hosts、配置高可用集群克隆多台模板机器运行并配置网卡

- 安装 JDK

略

- 安装 HadoopV3.0.3

> 配置 Hadoop 的`bin`和`sbin`到 path 即可
>
> 配置文件

` vim /etc/profile.d/software.sh`

```shell script
# !/bin/bash
export JAVA_HOME=/opt/module/jdk1.8.0_212
export HADOOP_HOME=/opt/module/hadoop-3.1.3

export PATH=$PATH:$JAVA_HOME/bin:$HADOOP_HOME/bin:$HADOOP_HOME/sbin
```

> 目录结构说明

```
bin: 存放对Hadoop相关服务（hdfs、yarn、MapReduce）进行操作的脚本
etc: Hadoop的配置文件目录, 存放Hadoop的配置文件
lib: 存放Hadoop的本地库(对数据进行压缩解压缩功能)
sbin: 存放启动或停止Hadoop相关服务的脚本
share: 存放Hadoop的依赖jar包,文档,和官方案例
```

# 拷贝环境到多台机器

- 拷贝 Java 和 Hadoop 到目标机器(不用执行)

> 通过 hostname 拷贝文件或文件夹

```shell
#!/bin/bash

# 工具名称
application_name=cptool

# 定义日志等级
error="[error - $application_name]: "

# 获取需要拷贝的源路径
source_dir=$1

# 文件不存在退出
if [[ -z $source_dir ]]; then
        echo $error source_dir cannot be null
        exit
else
        # 输入文件路径存在，找该文件 文件存在
        if [[ -d $source_dir || -f $source_dir ]]; then
                for node_num in {101..102}
                do
                        node=hadoop$node_num
                        scp -r $source_dir root@$node:$source_dir
                done
        # 文件不存在
        else
                echo $error filepath $source_dir not found
        fi
fi
```

- 配置 xsync

```shell
#!/bin/bash
#1. 判断参数个数
if [ $# -lt 1 ]
then
    echo Not Enough Arguement!
    exit;
fi
#2. 遍历集群所有机器
for host in hadoop101 hadoop102
do
    echo ==================== $host ====================
    #3. 遍历所有目录，挨个发送
    for file in $@
    do
    #4. 判断文件是否存在
    if [ -e $file ]
    then
        #5. 获取父目录
        pdir=$(cd -P $(dirname $file); pwd)
        #6. 获取当前文件的名称
        fname=$(basename $file)
        ssh $host "mkdir -p $pdir"
        rsync -av $pdir/$fname $host:$pdir
    else
        echo $file does not exists!
    fi
    done
done
```

- 配置免密登录

```shell
ssh-keygen -t rsa
ssh-copy-id {hostname}
```

# 运行 Hadoop

## 本地启动

> 本地启动仅作为体验用 我发使用 hdfs yarn 等组件(单机)

### 案例(wordcount)

- 在`${HADOOP_HOME}`创建`input/word.txt`文件夹及文件并输入字符

```text
bnyte
liujixiang
liuyang
shuaige
wozuishuaiqi
```

- 统计每个名字出现的次数

执行计算

```
hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-3.1.3.jar wordcount wcinput/ wcoutput
```

`wordcount`: 统计字符次数

`wcinput/`: 指定需要统计的文件所在的目录

`wcoutput`: 指定结果输出目录(如果文件已经存在则会直接报错),`_SUCCESS`文件用作标识本次执行成功,没有其他数据.

## 伪集群启动

> 伪集群可以使用 Hadoop 的所有功能且使用`SFTP`作为存储组件(单机)

## 集群启动

> 使用所有 Hadoop 组件功能并且支持多节点、高可用(集群模式)

### 集群配置

#### 集群规划

Tips:

> NameNode 和 SecondaryNameNode 不要安装在同一台服务器
>
> ResourceManager 也很消耗内存，不要和 NameNode、SecondaryNameNode 配置在
> 同一台机器上。

| 组件\机器 | hadoop100         | hadoop101                   | hadoop102                  |
| --------- | ----------------- | --------------------------- | -------------------------- |
| hdfs      | NameNode\DataNode | DataNode                    | SecondaryNameNode\DataNode |
| 计算组件  | NodeManager       | ResourceManager\NodeManager | NodeManager                |

#### 配置文件说明

Hadoop 配置文件分两类：默认配置文件和自定义配置文件，只有用户想修改某一默认
配置值时，才需要修改自定义配置文件，更改相应属性值。

- 默认配置文件

| 要获取的默认文件     | hadoop100                                                 |
| -------------------- | --------------------------------------------------------- |
| `core-default.xml`   | hadoop-common-3.1.3.jar/core-default.xml                  |
| `hdfs-default.xml`   | hadoop-hdfs-3.1.3.jar/hdfs-default.xml                    |
| `yarn-default.xml`   | hadoop-yarn-common-3.1.3.jar/yarn-default.xml             |
| `mapred-default.xml` | hadoop-mapreduce-client-core-3.1.3.jar/mapred-default.xml |

- 自定义配置文件

`core-site.xml`、`hdfs-site.xml`、`yarn-site.xml`、`mapred-site.xml` 四个配置文件存放在`$HADOOP_HOME/etc/hadoop` 这个路径上，用户可以根据项目需求重新进行修改配置。

- core-size.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<configuration>
    <!-- 指定 NameNode 的地址 -->
    <property>
        <name>fs.defaultFS</name>
        <value>hdfs://hadoop100:8020</value>
    </property>
    <!-- 指定 hadoop 数据的存储目录 -->
    <property>
        <name>hadoop.tmp.dir</name>
        <value>/opt/module/hadoop-3.1.3/data</value>
    </property>
    <!-- 配置 HDFS 网页登录使用的静态用户为 atguigu -->
    <property>
        <name>hadoop.http.staticuser.user</name>
        <value>bnyte</value>
    </property>
</configuration>
```

- hdfs-site.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<configuration>
    <!-- nn web 端访问地址-->
    <property>
        <name>dfs.namenode.http-address</name>
        <value>hadoop100:9870</value>
    </property>
    <!-- 2nn web 端访问地址-->
    <property>
        <name>dfs.namenode.secondary.http-address</name>
        <value>hadoop102:9868</value>
    </property>
</configuration>
```

- yarn-site.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<configuration>
    <!-- 指定 MR 走 shuffle -->
    <property>
        <name>yarn.nodemanager.aux-services</name>
        <value>mapreduce_shuffle</value>
    </property>
    <!-- 指定 ResourceManager 的地址-->
    <property>
        <name>yarn.resourcemanager.hostname</name>
        <value>hadoop101</value>
    </property>
    <!-- 环境变量的继承 -->
    <property>
        <name>yarn.nodemanager.env-whitelist</name>
        <value>JAVA_HOME,HADOOP_COMMON_HOME,HADOOP_HDFS_HOME,HADOOP_CONF_DIR,CLASSPATH_PREPEND_DISTCACHE,HADOOP_YARN_HOME,HADOOP_MAPRED_HOME</value>
    </property>
</configuration>
```

- mapred-site.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<configuration>
    <!-- 指定 MapReduce 程序运行在 Yarn 上 -->
    <property>
        <name>mapreduce.framework.name</name>
        <value>yarn</value>
    </property>
</configuration>
```

- 将配置好的配置分发给其他的节点

```shell
xsync /opt/module/hadoop3.1.3/etc/hadoop/
```

- 配置/opt/module/hadoop-3.1.3/etc/hadoop/workers

```shell
hadoop100
hadoop101
hadoop102
```

> 注意：这一步配置不可以有任何的空格

#### 群起集群

> 如果是第一次启动集群需要在`hadoop100`初始化`NameNode`(注意：格式
> 化 NameNode，会产生新的集群 id，导致 NameNode 和 DataNode 的集群 id 不一致，集群找
> 不到已往数据。如果集群在运行过程中报错，需要重新格式化 NameNode 的话，一定要先停
> 止 namenode 和 datanode 进程，并且要删除所有机器的 data 和 logs 目录，然后再进行格式
> 化。)

- 初始化集群(第一次启动需要)

```shell
hdfs namenode -format # 数据会被清空
```

- 启动集群

```shell
sh ${HADOOP_HOME}/sbin/start-dfs.sh
```

> 如果是使用`root`做的操作可能会报如下错

```
Starting namenodes on [hadoop100]
ERROR: Attempting to operate on hdfs namenode as root
ERROR: but there is no HDFS_NAMENODE_USER defined. Aborting operation.
Starting datanodes
ERROR: Attempting to operate on hdfs datanode as root
ERROR: but there is no HDFS_DATANODE_USER defined. Aborting operation.
Starting secondary namenodes [hadoop102]
ERROR: Attempting to operate on hdfs secondarynamenode as root
ERROR: but there is no HDFS_SECONDARYNAMENODE_USER defined. Aborting operation.
```

> 解决方案

- 对于 start-dfs.sh 和 stop-dfs.sh 文件，添加下列参数

```shell
HDFS_DATANODE_USER=root
HADOOP_SECURE_DN_USER=hdfs
HDFS_NAMENODE_USER=root
HDFS_SECONDARYNAMENODE_USER=root
```

- 对于 start-yarn.sh 和 stop-yarn.sh 文件，添加下列参数

```shell
#!/usr/bin/env bash
YARN_RESOURCEMANAGER_USER=root
HADOOP_SECURE_DN_USER=yarn
YARN_NODEMANAGER_USER=root
```

- 在配置了 ResourceManager 的节点`hadoop101`启动 YARN

```shell script
./sbin/start-yarn.sh
```

- Web 端访问`http://hadoop100:9870` HDFS 的 NameNode

- Web 端访问`http://hadoop101:8088`查看 YARN 的 ResourceManager

#### 集群基本测试

> 上传文件到集群

- 上传小文件

```shell script
hadoop fs -mkdir /input  # 在hdfs创建文件夹
hadoop fs -put ${HADOOP_HOME}/wcinput/word.txt /input # -put上传文件 本地文件 hdfs服务器路径
```

- 查看上传结果

```
1. 进入hdfs控制台界面`hadoop100:9870`
2. Utilities -> Browse the file system 查看文件系统
```

- 查看 hdfs 文件保存路径，查看三台集群储存的数据确认高可用特性

```shell script
cd ${HADOOP_HOME}/data/dfs/data/current/BP-739053608-192.168.100.100-1650959465447/current/finalized/subdir0/subdir0/
ll # 这个位置不带meta的文件就是数据文件了，在其他的集群也查看确认一下
```

- 从 hdfs 下载数据

> hadoop fs -get ${HDFS_FILEPATH} ${LOCAL_DOWNLOAD_PATH}

```
hadoop fs -get /input/word.txt ./
```

- 执行 wordcount 程序

```
# hadoop jar {execute_jar} {jarpath} {type} {loadfile} {execution_result_path}
hadoop jar /opt/module/hadoop-3.1.3/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.1.3.jar wordcount /input/word.txt /wc/output
```

#### 配置历史服务器

为了查看程序的历史运行情况，需要配置一下历史服务器。

- 配置`mapred-site.xml`

```
<!-- 历史服务器端地址 -->
<property>
    <name>mapreduce.jobhistory.address</name>
    <value>hadoop100:10020</value>
</property>
<!-- 历史服务器 web 端地址 -->
<property>
    <name>mapreduce.jobhistory.webapp.address</name>
    <value>hadoop100:19888</value>
</property>
```

- 分发配置

- 启动历史服务器

```shell script
mapred --daemon start historyserver
jps # 查看是否启动成功
```

- 访问历史服务器 web 端`http://hadoop100:19888/jobhistory`

#### 配置日志的聚集

日志聚集概念：应用运行完成以后，将程序运行日志信息上传到 HDFS 系统上

![](images/1.png)

> 开启日志聚集功能，需要重新启动 NodeManager、ResourceManager 和 HistoryServer

- 配置`yarn-site.xml`

```
<!-- 开启日志聚集功能 -->
    <property>
        <name>yarn.log-aggregation-enable</name>
        <value>true</value>
    </property>
    <!-- 设置日志聚集服务器地址 -->
    <property>
        <name>yarn.log.server.url</name>
        <value>http://hadoop100:19888/jobhistory/logs</value>
    </property>
    <!-- 设置日志保留时间为 7 天 -->
    <property>
        <name>yarn.log-aggregation.retain-seconds</name>
        <value>604800</value>
    </property>
```

- 分发配置

- 关闭 NodeManager、ResourceManager、HistoryServer

```shell script
stop-yarn.sh # 关闭yarn
mapred --deamon stop historyservice

start-yarn.sh # 启动yarn
mapred --daemon start historyserver
```

#### 集群时间同步

> 解决不同集群之中的所有集群时间不同这个时候 yarn 调度的时间不同其他节点发生冲突可能导致任务不会执行
>
> 如果服务器在公网环境（能连接外网），可以不采用集群时间同步，因为服务器会定期 和公网时间进行校准；
>
> 如果服务器在内网环境，必须要配置集群时间同步，否则时间久了，会产生时间偏差， 导致集群执行任务时间不同步。

- 需求

找一个机器，作为时间服务器，所有的机器与这台集群时间进行定时的同步，生产环境
根据任务对时间的准确程度要求周期同步。测试环境为了尽快看到效果，采用 1 分钟同步一
次。

![](images/2.png)

##### 时间服务器配置（必须 root 用户）

- 查看所有节点 ntpd 服务状态和开机自启动状态

```shell script
systemctl status ntpd
systemctl start ntpd
systemctl is-enabled ntpd
```

- 修改 `hadoop100` 的 `ntp.conf` 配置文件

```shell
sudo vim /etc/ntp.conf
```

修改 1（授权 192.168.100.0-192.168.100.255 网段上的所有机器可以从这台机器上查询和同步时间）

> restrict 192.168.100.0 mask 255.255.255.0 nomodify notrap

```shell
restrict 192.168.100.0 mask 255.255.255.0 nomodify notrap
```

修改 2（集群在局域网中，不使用其他互联网上的时间）

```shell
server 0.centos.pool.ntp.org iburst
server 1.centos.pool.ntp.org iburst
server 2.centos.pool.ntp.org iburst
server 3.centos.pool.ntp.org iburst
# 将上面配置改为如下配置
#server 0.centos.pool.ntp.org iburst
#server 1.centos.pool.ntp.org iburst
#server 2.centos.pool.ntp.org iburst
#server 3.centos.pool.ntp.org iburst
```

添加 3（当该节点丢失网络连接，依然可以采用本地时间作为时间服务器为集群中的其他节点提供时间同步）

```shell
server 127.127.1.0
fudge 127.127.1.0 stratum 10
```

- 修改 hadoop100 的/etc/sysconfig/ntpd 文件

```shell
sudo vim /etc/sysconfig/ntpd
```

增加内容如下（让硬件时间与系统时间一起同步）

```shell
SYNC_HWCLOCK=yes
```

- 重新启动 ntpd 服务

```shell
sudo systemctl start ntpd
```

- 设置 ntpd 服务开机启动

```shell
sudo systemctl enable ntpd
```

##### 其他机器配置（必须 root 用户）

- 关闭所有节点上 ntp 服务和自启动

```shell
sudo systemctl stop ntpd
sudo systemctl disable ntpd
sudo systemctl stop ntpd
sudo systemctl disable ntpd
```

- 在其他机器配置 1 分钟与时间服务器同步一次

```shell
 sudo crontab -e
```

- 编写定时任务如下：

```shell
*/1 * * * * /usr/sbin/ntpdate hadoop102
```

- 修改任意机器时间

```shell
sudo date -s "2021-9-11 11:11:11"
```

- 1 分钟后查看机器是否与时间服务器同步

```shell
sudo date
```
