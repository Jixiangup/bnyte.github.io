import json
import requests
import jwt
import time

# 读取密钥文件证书内容
f = open("/Users/kaisa.liu/workspaces/backend-infra-member-service/src/test/resources/SubscriptionKey_RRKLCRZ3PB.p8")
key_data = f.read()
f.close()

# JWT Header
header = {
    "alg": "ES256",
    "kid": "RRKLCRZ3PB",
    "typ": "JWT"
}

# JWT Payload
payload = {
    # 5177c9aa-2407-4d39-bbf2-3a0835edfdb6
    "iss": "5177c9aa-2407-4d39-bbf2-3a0835edfdb6",
    "aud": "appstoreconnect-v1",
    "iat": int(time.time()),
    "exp": int(time.time()) + 60 * 60,  # 60 minutes timestamp
    "bid": "test.novaverse.ios"
}

# JWT token
token = jwt.encode(headers=header, payload=payload,
                   key=key_data, algorithm="ES256")

# JWT Token

# 请求链接和参数
url = "https://api.storekit-sandbox.itunes.apple.com/inApps/v1/subscriptions/2000000292917185"
header = {
    "Authorization": f"Bearer {token}"
}

# 请求和响应
rs = requests.get(url, headers=header)
data = json.loads(rs.text)

print(jwt.decode(data['data'][0]['lastTransactions']
      [0]['signedTransactionInfo'], algorithms=''))
