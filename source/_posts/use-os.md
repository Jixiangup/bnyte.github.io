---
title: 系统使用
date: 2022-06-16 13:03:18
tags: 连载
---

本文主要连载一些系统包括`Windows`,`Linux`,`Mac`等系统日常使用中遇到或写的一些小脚本或者说一些使用技巧等等~

<!-- more -->

# Changelog

## 20220708

- [SublimeText3连接SFTP](#SublimeText3连接SFTP)

## 20220708之前

- [Windows微信多开](#微信多开)
- [科学使用Jetbrains](#科学使用Jetbrains)


# Windows

## 微信多开

- 创建`.bat`可执行脚本文件。

- 找到`wechat.exe`的目标地址

- 键入如下脚本

```powershell
TASKKILL /F /IM wechat.exe
start "" "D:\Tencent\WeChat\WeChat.exe" rem 需要多开的目标地址
start "" "D:\Tencent\WeChat\WeChat.exe" rem 需要多开的目标地址
```

# Mac

# Linux

# 通用

## SublimeText3连接SFTP

- 下载安装Sublime text3

- `Ctrl+\``打开控制台输入如下代码

```
import urllib.request,os,hashlib; h = '2915d1851351e5ee549c20394736b442' + '8bc59f460fa1548d1514676163dafc88'; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); by = urllib.request.urlopen( 'http://packagecontrol.io/' + pf.replace(' ', '%20')).read(); dh = hashlib.sha256(by).hexdigest(); print('Error validating download (got %s instead of %s), please try manual install' % (dh, h)) if dh != h else open(os.path.join( ipp, pf), 'wb' ).write(by)
```

- Preferences -> Browse Packages.....弹出目录后, 下载[插件](https://packagecontrol.io/Package Control.sublime-package)或访问浏览器下载`https://packagecontrol.io/Package Control.sublime-package`, 下载完成之后直接将其复制到刚刚打开的文件当中重启

- `Ctrl+Shift+P`调出命令面板输入`install package`按回车等待弹出新的控制弹窗

- 在弹出的控制弹窗中输入`SFTP`回车等待下载完成

- 安装完成之后点击 `File -> SFTP/FTP -> MapToRemote 或者 Edit Server`

- 自动生成一个sftp-config.json文件, 结合自己的情况配置就可以了

## 科学使用Jetbrains

> 下面的功能没有特殊标注则表明支持`jetbrains`家族下面的所有系列产品均可通用~

### 使用`Reset`插件重置

> 仅支持2021.3以下 建议使用2021.2.x版本

### 下载idea

> [点击下载idea](https://download.jetbrains.com/idea/ideaIU-2021.2.2.exe?_gl=1*1c4chbw*_ga*MTA0ODE1ODkwNS4xNjM1NTkwMzE3*_ga_V0XZL7QHEB*MTY0ODM4OTgxNC40LjEuMTY0ODM4OTgyMC4w&_ga=2.223952603.1391899983.1648389815-1048158905.1635590317)

如果点击下载没有反应可以前往[官网](https://www.jetbrains.com/zh-cn/idea/download/other.html)下载

![](https://blogimg.bytestroll.com/blog_img/idea/1.png)

### 安装

- 卸载老版本

![](https://img.chajianxw.com/chajian/164604171691955)

![](https://img.chajianxw.com/chajian/164604174406150)

安装就是无脑安装下一步(`next`)就可以了..没什么好说的

- 开始安装

![](https://img.chajianxw.com/chajian/164604330408118)

![](https://img.chajianxw.com/chajian/164604335389359)

![](https://img.chajianxw.com/chajian/164604339538384)

![](https://img.chajianxw.com/chajian/164604343562437)

![](https://img.chajianxw.com/chajian/164604347765732)

> 如果没有试用三十天请自行降低版本


### 使用

- 安装完成之后打开

- 打开插件

![](https://blogimg.bytestroll.com/blog_img/idea/2.png)

- 添加仓库插件仓库地址`plugins.zhile.io`

![](https://blogimg.bytestroll.com/blog_img/idea/3.png)

- 搜索插件`IDE Eval Reset`

![](https://blogimg.bytestroll.com/blog_img/idea/4.png)

- 开启`插件`

![](https://blogimg.bytestroll.com/blog_img/idea/5.png)

> 等待重启，成功，每次`重启`就会重新`刷新试用时间`了

# Thanks

- 感谢`CSDN`用户[ZFH__ZJ](https://blog.csdn.net/ZJ__ZFH)