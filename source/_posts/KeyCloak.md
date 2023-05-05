---
layout: keycloak
title: KeyCloak
date: 2023-04-28 17:33:39
tags: [学习]
---

# KeyCloak

Keycloak 是一个开源软件产品，旨在为现代的应用程序和服务，提供包含身份管理和访问管理功能的单点登录工具。截至 2018 年 3 月，红帽公司负责管理这一 JBoss 社区项目，并将其作为他们 RH-SSO 产品的上游项目。从概念的角度上来说，该工具的目的是，只用少量编码甚至不用编码，就能很容易地使应用程序和服务更安全。

<!-- more -->

## 安装

### Docker

#### 在你开始之前

请确保安装了 Docker

#### 启动 keycloak

初始化启动并暴露本地端口`8080`, 并指定管理员账号密码为`admin`

```sh
docker run -p --name keycloak 8080:8080 -e KEYCLOAK_ADMIN=admin -e KEYCLOAK_ADMIN_PASSWORD=admin quay.io/keycloak/keycloak start-dev
```

- KEYCLOAK_ADMIN 管理后台账号
- KEYCLOAK_ADMIN_PASSWORD 管理后台密码

## 基础使用

### 登陆管理控制台

- 转到 [Keycloak 管理控制台](http://localhost:8080/admin)。

- 使用您之前创建的用户名和密码登录。

### 创建 realm

Keycloak 中的 realm 相当于一个租户。每个领域都允许管理员创建隔离的应用程序和用户组。最初，Keycloak 包含一个名为 master. 仅将此领域用于管理 Keycloak，而不用于管理任何应用程序。

使用这些步骤创建第一个 realm。

1. 打开 [Keycloak 管理控制台](http://localhost:8080/admin)。
2. 单击左上角的`master`一词，然后单击`Create realm`，创建名为`myrealm`的一个新的 realm。

![add-realm](https://storage.bnyte.com/blog_img/keycloak/add-realm.png)

### 创建用户

默认情况下 realm 是没有用户的，所以需要手动创建。

1. 打开 [Keycloak 管理控制台](http://localhost:8080/admin)。
2. 单击左侧菜单中的`Users` -> `Add user`

```
创建用户时参数介绍
Required user actions: 用户第一次登陆触发的行为，比如验证邮箱、更新密码等等。可以为空
Username：用户名(用于登陆)
Email: 邮箱地址，可以为空
Email verified: 电子邮件地址是否已经得到验证
First name: 姓?又或者名？这种定义很模糊，所以我也不确定，不过在最后获取到名称是 FirstName + LastName
Last name
Groups: 权限组，可以为空
```

创建用户之后需要设置密码之后才能登陆，所以还需要设置初始密码

1. 进入用户详情点击顶部的`Credentials`然后设置一个密码并且保存即可。

### 登陆账户控制台

现在可以登陆到账户控制台以验证此用户是否已正确配置。

1. 打开 [Keycloak 帐户控制台](http://localhost:8080/realms/myrealm/account)。

> 当然如果你在创建`realm`时名称不是`myrealm`时你只需要按照以下方式改变这个路径就可以访问: `http://localhost:8080/realms/${realm}/account`

2. 使用你之前创建的用户名和密码登录即可。
