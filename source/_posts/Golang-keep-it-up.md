---
title: Golang-keep_it_up
date: 2022-12-05 12:29:35
tags: [学习, 连载]
---

本文主要连载自己的`Golang`学习笔记以及自己遇到的一些坑或者说自己的感悟吧, 这是一个漫长的过程, 如同标题一样 `keep it up gogogo....`

<!-- more -->

# 引言

> 其实本来不打算写这个引言 既然是blog 还是写写吧 并不是笔记项目哈哈哈，学这个就是最近学完了`python`然后想再继续学点吧, 毕竟都说它是`Google`开源的未来趋势，毕竟`k8s`, `docker`等前沿或者应用较为广泛的技术都被应用上了, 而我还在守着`Java`的一亩三分地自顾自的说着`Java No.1`倒是有些顽固不化了，说那么多，就不说了 开始吧！！！！

> 本文主要素材内容来源于网络,主要采取[Golang官方文档](https://go.dev), 如果引用了其他帮助请见下文的[鸣谢](#鸣谢)，如果我标记错了出处或者对您的版权产生了侵犯，请您谅解我并非有意，这并非一个`商用博客`，同时您如果对此有任何不满请与[我](/about)取得联系, 我将以最快的时间之内对您进行处理，因为我需要工作所以希望您能够耐心的等待。

# Golang

## 环境准备

### 选择IDE

  我是使用的[JetBrains](https://www.jetbrains.com/)公司产出的`GoLand`进行开发，如果你期望使用[VsCode](https://code.visualstudio.com/)你可以自行获取解决、集成方案。

### 安装Golang

  在[Golang官方下载](https://go.dev/dl/)页下载适合自己系统适用的环境版本, 并且打开直接下一步安装即可。

配置环境变量以及简单创建文件的配置就忽略了...

### HelloWorld

创建空文件夹使用`goland`打开，或者直接在`goland`中创建工程.

- 在项目根目录创建文件`go.mod`
  
  ```
  // 模块名可以直接与工程名相同
  module helloworld
  ```

- 创建main.go文件

- 编写`main`函数

  ```go
  // 没个项目都必须要有一个，并且如果期望运行必须引入且方法中必须包含`main`函数
  package main

  import "fmt"

  func main() {
    fmt.Println("Hello World")
  }
  ```
# 语法总结

- 不需要使用分号

# 踩坑

- 在`Go`里面必须要配置的是`GOROOT`和`GOPATH`

  ```
  GOROOT: go安装的根路径
  GOPATH: 暂时不知道作用是什么到时候补上
  ```

# 鸣谢

- [Golang](https://go.dev)
- [JetBrains](https://www.jetbrains.com/)
