---
layout: mongo
title: MongoDB
date: 2023-03-22 11:18:41
tags:
---

本文连载`mongodb`学习以及使用经验等相关笔记

<!-- more -->

# 快速开始

## Docker

### 运行容器

```
docker run -itd --name mongo -p 27017:27017 mongo --auth
```

> 参数解释

- --auth 则表示使用密码才能登录访问

### 配置

- 基础配置

```shell
# 进入容器 如果高于6.0版本使用 docker exec -it mongo mongosh admin
docker exec -it mongo mongo admin

# 创建一个名为 admin，密码为 123456 的超级用户。
db.createUser({ user:'admin',pwd:'123456',roles:[ { role:'userAdminAnyDatabase', db: 'admin'},"readWriteAnyDatabase"]});

# 尝试使用上面创建的用户信息进行连接 返回1则表示成功
db.auth('admin', '123456');
```

- 配置远程访问

```bash
docker exec -it mongo bash

apt-get update

apt-get install vim
#修改 mongo 配置文件
vim /etc/mongod.conf.orig
```

将其中的`bindIp: 127.0.0.1`注释掉`# bindIp: 127.0.0.1` 或者改成 `bindIp: 0.0.0.0` 即可开启远程连接
