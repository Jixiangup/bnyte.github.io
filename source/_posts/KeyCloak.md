---
layout: keycloak
title: KeyCloak
date: 2023-04-28 17:33:39
tags: [学习]
---

# KeyCloak

Keycloak 是一个开源软件产品，旨在为现代的应用程序和服务，提供包含身份管理和访问管理功能的单点登录工具。截至 2018 年 3 月，红帽公司负责管理这一 JBoss 社区项目，并将其作为他们 RH-SSO 产品的上游项目。从概念的角度上来说，该工具的目的是，只用少量编码甚至不用编码，就能很容易地使应用程序和服务更安全。

[代码仓库](https://github.com/bnyte/keyclock-example)

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

## 应用到项目当中

> 这是一个先觉条件，你需要先创建好 client 才能应用到项目当中去

- `Clients` -> `Create client`
- 配置信息

  Step 1

  ```
  Client type: 客户端类型，有两个选项我也还在研究先用默认的吧。
    - OpenId Connect:
    - SAML:
  Client ID: 这是一个必填项，你需要自行配置，但是这是有用的。指定 URI 和令牌中引用的 ID。例如“我的客户端”。对于 SAML，这也是来自 authn 请求的预期颁发者值
  Name: 指定客户端的显示名称。例如“我的客户端”。也支持本地化值的键。例如：${my_client}
  Description: 指定客户端的描述。例如“我的时间表客户端”。也支持本地化值的键。例如：${my_client_description}
  Always display in UI: 始终在帐户 UI 中列出此客户端，即使用户没有活动会话。【不知道干啥用的】
  ```

  Step 2

  ```
  这一步的配置我都还没有研究，我直接下一步的，有时间研究一下。
  ```

  Step 3

  ```
  Root URL: 附加到相对 URL 的根 URL，这里先暂时不配置
  Home URL: 当 auth 服务器需要重定向或链接回客户端时使用的默认 URL。这里也暂时先不配置
  Valid redirect URIs: 成功登录后浏览器可以重定向到的有效 URI 模式。允许使用简单的通配符，例如“http://example.com/*”。也可以指定相对路径，例如/my/relative/path/*。相对路径是相对于客户端根 URL 的，或者如果没有指定，则使用身份验证服务器根 URL。对于 SAML，如果您依赖登录请求中嵌入的消费者服务 URL，则必须设置有效的 URI 模式。如刚刚我是用的是umijs，而这里的值只需要加入一个"http://127.0.0.1:8000/*"。
  Valid post logout redirect URIs: 成功注销后浏览器可以重定向到的有效 URI 模式。“+”值或空字段将使用有效重定向 URI 列表。“-”值将不允许任何注销后重定向 uris。允许使用简单的通配符，例如“http://example.com/*”。也可以指定相对路径，例如/my/relative/path/*。相对路径是相对于客户端根 URL 的，或者如果没有指定，则使用身份验证服务器根 URL。暂时还不知道干啥用的。
  Web origins: 允许的 CORS 来源。要允许有效重定向 URI 的所有来源，请添加“+”。不过，这不包括“*”通配符。要允许所有来源，请明确添加“*”。如刚刚我是用的是umijs，而这里的值只需要加入一个"http://127.0.0.1:8000/*"。
  ```

- 创建完成之后进入`Client Detail`点击右上角`Action` -> `Download adaptor configs`即可获取到详细的配置。

当然，在前端项目中我们登陆之后可以获取到 KeyCloak 的实例对象，而他的实例对象值包含如下结果

```json
{
  "authenticated": true,
  "loginRequired": true,
  "silentCheckSsoFallback": true,
  "enableLogging": false,
  "messageReceiveTimeout": 10000,
  "responseMode": "fragment",
  "responseType": "code",
  "flow": "standard",
  "clientId": "example",
  "authServerUrl": "http://localhost:8080/",
  "realm": "example",
  "endpoints": {},
  "refreshToken": "eyJhbGciOiJIUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICI0NjZmMWQ5NS0wN2Q5LTQ3ZTAtYWIzNi1jMDZlNzA1NDRkZjAifQ.eyJleHAiOjE2ODMyNjEzMDIsImlhdCI6MTY4MzI1OTUwMiwianRpIjoiMmM0OWQ2ZmMtZjg5OS00ODgzLTg4ZDMtNjNiODJkOTY0MGNiIiwiaXNzIjoiaHR0cDovL2xvY2FsaG9zdDo4MDgwL3JlYWxtcy9leGFtcGxlIiwiYXVkIjoiaHR0cDovL2xvY2FsaG9zdDo4MDgwL3JlYWxtcy9leGFtcGxlIiwic3ViIjoiNmMzMDIzNGUtY2IxNi00NDZlLTk0YzAtY2QwM2FjZmUyMzFhIiwidHlwIjoiUmVmcmVzaCIsImF6cCI6ImV4YW1wbGUiLCJub25jZSI6IjY2MWIyNjkyLWJjNDItNDk5OS1hMDViLTZkODIxY2I0NTdkZCIsInNlc3Npb25fc3RhdGUiOiIwNGI1NmU2NS0wYTg1LTRiMTMtODhlNi02NTdmYjk5YzJlZDUiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwic2lkIjoiMDRiNTZlNjUtMGE4NS00YjEzLTg4ZTYtNjU3ZmI5OWMyZWQ1In0.OdzfDO2DM1if_4_0CcuJl_JLOoJYAnR3ABkWzsv5vgw",
  "refreshTokenParsed": {
    "exp": 1683261302,
    "iat": 1683259502,
    "jti": "2c49d6fc-f899-4883-88d3-63b82d9640cb",
    "iss": "http://localhost:8080/realms/example",
    "aud": "http://localhost:8080/realms/example",
    "sub": "6c30234e-cb16-446e-94c0-cd03acfe231a",
    "typ": "Refresh",
    "azp": "example",
    "nonce": "661b2692-bc42-4999-a05b-6d821cb457dd",
    "session_state": "04b56e65-0a85-4b13-88e6-657fb99c2ed5",
    "scope": "openid profile email",
    "sid": "04b56e65-0a85-4b13-88e6-657fb99c2ed5"
  },
  "idToken": "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJ6SDNXLVo4TGhaR0F2WWE3S2NKOHJJalYzdXhGZi0xVFRadks0ZUVnaWFFIn0.eyJleHAiOjE2ODMyNTk4MDIsImlhdCI6MTY4MzI1OTUwMiwiYXV0aF90aW1lIjoxNjgzMjU5NDk3LCJqdGkiOiI4NDkxMWFiOS00NzM4LTQwNmUtYmQzNS05NmRlY2VhZjM2MTgiLCJpc3MiOiJodHRwOi8vbG9jYWxob3N0OjgwODAvcmVhbG1zL2V4YW1wbGUiLCJhdWQiOiJleGFtcGxlIiwic3ViIjoiNmMzMDIzNGUtY2IxNi00NDZlLTk0YzAtY2QwM2FjZmUyMzFhIiwidHlwIjoiSUQiLCJhenAiOiJleGFtcGxlIiwibm9uY2UiOiI2NjFiMjY5Mi1iYzQyLTQ5OTktYTA1Yi02ZDgyMWNiNDU3ZGQiLCJzZXNzaW9uX3N0YXRlIjoiMDRiNTZlNjUtMGE4NS00YjEzLTg4ZTYtNjU3ZmI5OWMyZWQ1IiwiYXRfaGFzaCI6IjhnYTdSckZiSndQSXluQVB2OC1CanciLCJhY3IiOiIwIiwic2lkIjoiMDRiNTZlNjUtMGE4NS00YjEzLTg4ZTYtNjU3ZmI5OWMyZWQ1IiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJkZXYiLCJnaXZlbl9uYW1lIjoiIiwiZmFtaWx5X25hbWUiOiIifQ.RHgN90yoqTnXrSzN-_cIMomzFdb689_lBCfpKR6Idl07qQ22QK0YcJ2Npmlln2-dgHdeE9je6wqTD8c_RSGFGifji7hfLzoghipS0gzC-oxfvzhUb32-8HMMPQfSoor81qY-5i0LgCIbLC-j5POLm8OuzED69i2gRu1lAuG_BUCspLBLC7ylsfVNX_5nMVgv-Th65aJShi6AcZVuGLmKmurKac1kuGosXLVXk44Jv9OEQ5fko_ToEz8eIMHefgOUyqw6bXE0Q-_BDjRc_ZByZOAVW49S13WYLlotine_-ImN8yqZ2D-ELFF4gr0UyNOf9H8hi5TucdWKRomoNyY-OA",
  "idTokenParsed": {
    "exp": 1683259802,
    "iat": 1683259502,
    "auth_time": 1683259497,
    "jti": "84911ab9-4738-406e-bd35-96deceaf3618",
    "iss": "http://localhost:8080/realms/example",
    "aud": "example",
    "sub": "6c30234e-cb16-446e-94c0-cd03acfe231a",
    "typ": "ID",
    "azp": "example",
    "nonce": "661b2692-bc42-4999-a05b-6d821cb457dd",
    "session_state": "04b56e65-0a85-4b13-88e6-657fb99c2ed5",
    "at_hash": "8ga7RrFbJwPIynAPv8-Bjw",
    "acr": "0",
    "sid": "04b56e65-0a85-4b13-88e6-657fb99c2ed5",
    "email_verified": false,
    "preferred_username": "dev",
    "given_name": "",
    "family_name": ""
  },
  "token": "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJ6SDNXLVo4TGhaR0F2WWE3S2NKOHJJalYzdXhGZi0xVFRadks0ZUVnaWFFIn0.eyJleHAiOjE2ODMyNTk4MDIsImlhdCI6MTY4MzI1OTUwMiwiYXV0aF90aW1lIjoxNjgzMjU5NDk3LCJqdGkiOiJmY2FmNGQ0MC1iZjI3LTRiZWUtYWVjMC04MmRkODA2ZDgzZGEiLCJpc3MiOiJodHRwOi8vbG9jYWxob3N0OjgwODAvcmVhbG1zL2V4YW1wbGUiLCJhdWQiOiJhY2NvdW50Iiwic3ViIjoiNmMzMDIzNGUtY2IxNi00NDZlLTk0YzAtY2QwM2FjZmUyMzFhIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoiZXhhbXBsZSIsIm5vbmNlIjoiNjYxYjI2OTItYmM0Mi00OTk5LWEwNWItNmQ4MjFjYjQ1N2RkIiwic2Vzc2lvbl9zdGF0ZSI6IjA0YjU2ZTY1LTBhODUtNGIxMy04OGU2LTY1N2ZiOTljMmVkNSIsImFjciI6IjAiLCJhbGxvd2VkLW9yaWdpbnMiOlsiaHR0cDovLzEyNy4wLjAuMTo4MDAwIl0sInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJvZmZsaW5lX2FjY2VzcyIsImRlZmF1bHQtcm9sZXMtZXhhbXBsZSIsInVtYV9hdXRob3JpemF0aW9uIl19LCJyZXNvdXJjZV9hY2Nlc3MiOnsiYWNjb3VudCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInNpZCI6IjA0YjU2ZTY1LTBhODUtNGIxMy04OGU2LTY1N2ZiOTljMmVkNSIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwicHJlZmVycmVkX3VzZXJuYW1lIjoiZGV2IiwiZ2l2ZW5fbmFtZSI6IiIsImZhbWlseV9uYW1lIjoiIn0.ZcdXjq78rTa2liT1GTu5pwf6Rnm8s50GHB0xcavZydjw5WNCG2CUuDqszM_ZJSlbPZ99bZ83GHuu64CVk37EjHBI8wjFKRK_jr5IZ4OBCilmAZ2Q_y13cPFD3tDdlxpxBVcQzdcPYmIVrU3KvHRRsurvYPETbQFoqSqRDwTb-MePEKZMkNgt11c3us1gf06EMT-UpZ7yJIF4vBhorZp_hZNv-ZLXQ7NW9FZfnMNp2HrlPmoAbqQJ6PXDyjXInDvRXbC9fxkNLhtD4b-YCHtJViotMSeLjzo_viJA4Al5wmR8rv2EYgMSHa3HToyMOalVl2QubSAqVRqMUdMEUGxwsQ",
  "tokenParsed": {
    "exp": 1683259802,
    "iat": 1683259502,
    "auth_time": 1683259497,
    "jti": "fcaf4d40-bf27-4bee-aec0-82dd806d83da",
    "iss": "http://localhost:8080/realms/example",
    "aud": "account",
    "sub": "6c30234e-cb16-446e-94c0-cd03acfe231a",
    "typ": "Bearer",
    "azp": "example",
    "nonce": "661b2692-bc42-4999-a05b-6d821cb457dd",
    "session_state": "04b56e65-0a85-4b13-88e6-657fb99c2ed5",
    "acr": "0",
    "allowed-origins": ["http://127.0.0.1:8000"],
    "realm_access": {
      "roles": ["offline_access", "default-roles-example", "uma_authorization"]
    },
    "resource_access": {
      "account": {
        "roles": ["manage-account", "manage-account-links", "view-profile"]
      }
    },
    "scope": "openid profile email",
    "sid": "04b56e65-0a85-4b13-88e6-657fb99c2ed5",
    "email_verified": false,
    "preferred_username": "dev",
    "given_name": "",
    "family_name": ""
  },
  "sessionId": "04b56e65-0a85-4b13-88e6-657fb99c2ed5",
  "subject": "6c30234e-cb16-446e-94c0-cd03acfe231a",
  "realmAccess": {
    "roles": ["offline_access", "default-roles-example", "uma_authorization"]
  },
  "resourceAccess": {
    "account": {
      "roles": ["manage-account", "manage-account-links", "view-profile"]
    }
  },
  "timeSkew": 0
}
```

### 应用到前端(React)

这里前端脚手架采用的是 [Umijs](https://umijs.org/) 详细介绍和使用文档请参考 [Umijs](https://umijs.org/) 官方文档。

- 初始化项目

```
yarn create umi
```

- 添加必要依赖项

```
yarn add @umijs/plugins
yarn add keycloak-js
```

- 在 `src` 下面创建`app.ts`

`src/app.ts`

```typescript
import Keycloak from "keycloak-js";

/**
 * 初始化客户端，并且携带数据保存包含nickname和keycloak实例对象
 * @see  https://umijs.org/zh-CN/plugins/plugin-initial-state
 */
export async function getInitialState(): Promise<{
  nickname: string | undefined;
  keycloak: Keycloak;
}> {
  // 这个配置从client detail中获取
  const keycloak: Keycloak = new Keycloak({
    // 取 auth-server-url
    url: "http://127.0.0.1:8080/",
    // 取 realm
    realm: "example",
    // 取 resource
    clientId: "example",
  });
  let nickname;
  // 初始化keycloak
  const auth = await keycloak.init({ onLoad: "login-required" });
  if (!auth) {
    window.location.reload();
  } else {
    // username 登陆用户名
    // nickname = keycloak.tokenParsed?.preferred_username;
    // all name 姓名
    nickname = keycloak.tokenParsed?.name;
    // family name 姓
    // nickname = keycloak.tokenParsed?.family_name;
    // given name 名
    // nickname = keycloak.tokenParsed?.given_name;
  }
  return {
    nickname,
    keycloak,
  };
}
```

- 在 `src/pages` 下创建 `index.tsx`

`src/pages/index.tsx`

```typescript
import { useModel } from "umi";

export default function HomePage() {
  const { initialState } = useModel("@@initialState") ?? {};
  console.log("initialState", initialState);
  return (
    <div>
      <h1>{initialState?.nickname}</h1>
      <button
        onClick={() => {
          console.log("keycloak对象", initialState?.keycloak);
          console.log("nickname", initialState?.nickname);
        }}
      >
        Login
      </button>
      <button
        onClick={() => {
          initialState?.keycloak.logout();
        }}
      >
        Logout
      </button>
    </div>
  );
}
```

- 至此整合就完成了，其他功能再发现吧
