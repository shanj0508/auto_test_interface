import requests
import json

# 请求数据的准备
url = 'http://dev.product.sysware.com.cn/eap/doLogin.action'
headers = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
}
data = {
    'loginName': 'admin',
    'loginPassword': 'e8UK2S+2Y5qlN6R4A6KjuguLgwwts+oRe9t73w+PT9erNQfXc79C+ZbC4IXhPjJcwetxUypXuUW32PCIe9aaxQKF+wkBJJs000/Lkeg3Be2MvXeGgQxxOWGBu+jFBkeB0T7/UWAK7NJsKspqBS/H67wol9Znb3nqkGqBXsp73ok='
}

# 模拟请求的下发
res = requests.post(url=url, data=data)
# 如果请求体是json格式，这里可以直接写为：res = requests.post(url=url, json=data),这样就不用单独再headers中设置为json格式了

# 解析响应结果，判断本次接口的请求是否成功
print(res.text)
print(type(res.text))
print(json.loads(res.text)['success'])
print(type(json.loads(res.text)))
print(res)
# 通过断言校验本次测试是否成功
msg = True
# assert msg == json.loads(res.text)['success'],'断言失败'
assert msg == res.json()['success'],'断言失败'
