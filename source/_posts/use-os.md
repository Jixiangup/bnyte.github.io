---
title: 系统使用
date: 2022-06-16 13:03:18
tags: 连载
---

本文主要连载一些系统包括`Windows`,`Linux`,`Mac`等系统日常使用中遇到或写的一些小脚本或者说一些使用技巧等等~

<!-- more -->

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