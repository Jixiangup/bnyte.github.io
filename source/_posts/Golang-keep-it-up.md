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

## 语法介绍

### 创建函数

- 语法

  主意：当返回值为`void`时直接缺省。

  > func {FUNC_NAME}({NAME} {TYPE}, .... {NAME} {TYPE}) {RESULT_TYPE} { code block... }

  ```go
  func sum(pre int, next int) int {
    return pre + next;
  }
  ```

### 创建变量

- 指定变量类型，如果没有初始化，则变量默认为零值

  > var {field_name} {field_type}
  > 
  > {field_name} = {field_value}

  ```go
  package main
  import "fmt"

  func main() {
    var name = "猪猪侠"
    fmt.Println("用户名是:", name) // 猪猪侠

    var b int
    fmt.Println("没有初始化值的b:", b) // 0

    var c bool
    fmt.Println("没有初始化值的c", false) // boolean类型默认为false
  }
  ```
- 隐式生命语法糖

  主意：无法使用在已经使用`var`声明过的属性上

  > {field_name} := {field_value}

  ```go
  // 等价 var number int = 1
  number := 1
  ```

- 多变量声明

  > 类型相同的多个变量，非全局变量

  ```go
  // 等价于 name00, name01 := 1, 2
  var name00, name01 int = 1, 2

  // 这种因式分解关键字的写法一般用于声明全局变量
  const (
      vname1 v_type1
      vname2 v_type2
  )
  ```


<!-- arr1 := [...]int{1, 2, 3} -->

- 总结

  当函数、属性名的首字母大写时，则该实例会被导出(如Java中的`public`)

## 本地多模块

- 创建模块

```
go mod init bnyte.com/hello
```

- 指定查找依赖项

> 模块名 = 模块给予当前路径的路径

```
 go mod edit -replace bnyte.com/greetings=../greetings
```

- 指定模块使用本地模块以及版本

```
go mod tidy
```

## 异常

- 抛出异常

  ```go
  package main

  import "errors"

  func main() {
    errors.New("empty name")
  }
  ```

- 打印异常并中断程序执行

  ```go
  package main

  import (
    "errors"
    "log"
  )

  func main() {
    err := errors.New("empty name")

    // 设置预定义Logger的属性，包括
    // 日志条目前缀和禁用打印的标志
    //  时间、源文件和行号.
    log.SetPrefix("greetings: ")
	  log.SetFlags(10)
    log.Fatal(err)
  }
  ```

# 语法总结

- 不需要使用分号
- 在go中的名称具有语义效果，名称在包外的可见性取决于它的第一个字符是否大些。
- 导入包时，包名称成为内容的访问器如：
  ```go
  import "fmt"

  func main() {
    fmt.Println("包名访问方式");
  }
  ```
- 导入包时同时可以指定别名:
  ```go
  import "f fmt"

  func main() {
    f.Println("包名访问方式");
  }
  ```
- 在Go中是不允许忽略`{}`(大括号)的，即使代码块中只有一行。

# Go总结

- 在 Go 中`string`同样属于基本数据类型，使用这些类型的变量直接指向存在内存中的值, 通过`&{field_name}`来获取到对象内存地址，与此同时值类型变量的值`存储在堆`中。

- 在 Go 通过`*{field_name}`来获取到内存所对应的值。

# 踩坑

- 在`Go`里面必须要配置的是`GOROOT`和`GOPATH`

  ```
  GOROOT: go安装的根路径
  GOPATH: 暂时不知道作用是什么到时候补上
  ```

# 鸣谢

- [Golang](https://go.dev)
- [JetBrains](https://www.jetbrains.com/)
