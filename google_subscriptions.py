import json
import requests

subscriptions_url = "https://androidpublisher.googleapis.com/androidpublisher/v3/applications/{packageName}/purchases/subscriptions/{subscriptionId}/tokens/{token}{type}"

product_url = "https://androidpublisher.googleapis.com/androidpublisher/v3/applications/{packageName}/orders/{orderId}{type}"
get_token_url = "https://oauth2.googleapis.com/token"
get_token_header = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': '*/*',
}
get_token_data = {
    "client_id": "831027528014-2a5732umsjjtsr9o8kng40k988bc97no.apps.googleusercontent.com",
    "client_secret": "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",
    "grant_type": "refresh_token",
    "refresh_token": "1//0eluFYkSzGt5SCgYIARAAGA4SNwF-L9IrsMrdq5pXlwA0QLXPddtZUb-666E319lQtkAn3YwwnTVo-E0VsV30iP6sVrxw0-mZffw"
}
token_resp = requests.post(
    get_token_url, headers=get_token_header, data=get_token_data)


package_name = "test.novaverse.android"
# 这是鉴权token
access_token = json.loads(token_resp.text)['access_token']
print(access_token)
type = ':refund'

# t_vip 表的 goods_no
subscription_id = ""

subscription_headers = {
    "Authorization": "Bearer {access_token}".format(access_token=access_token)
}
order_id = 'GPA.3389-8978-1226-38817'

token = 'aojghbbcpkdbffapafghamoo.AO-J1Oz0AfZpT4QChp0wsHPz5jS8hLLuWA35zpfbVaGwRC3ENlTiRJaTbnfQ9wpejmzd9CrwKYugKeWswHLXhjpEhBouaKgADIMg5YZSD-KGR7h8OnZT02M'

# 发get请求就是获取订单信息
# 其他post请看文档 https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptions/revoke?hl=zh-cn
subscription_resp = requests.post(subscriptions_url.format(
    packageName=package_name, subscriptionId=subscription_id,
    token=token, type=type), headers=subscription_headers)

subscription_resp = requests.post(product_url.format(
    packageName=package_name, orderId=order_id,
    token=token, type=type), headers=subscription_headers)

print(subscription_resp.text)
