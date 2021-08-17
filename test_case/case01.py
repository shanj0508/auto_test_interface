from aip_key.api import ApiDemo

ad = ApiDemo()

# 请求数据的准备
url = 'http://dev.product.sysware.com.cn/eap/doLogin.action'
data = {
    'loginName': 'admin',
    'loginPassword': 'e8UK2S+2Y5qlN6R4A6KjuguLgwwts+oRe9t73w+PT9erNQfXc79C+ZbC4IXhPjJcwetxUypXuUW32PCIe9aaxQKF+wkBJJs000/Lkeg3Be2MvXeGgQxxOWGBu+jFBkeB0T7/UWAK7NJsKspqBS/H67wol9Znb3nqkGqBXsp73ok='
}

# 模拟请求的下发
res = ad.do_post(url=url, data=data)

# 解析响应结果，判断本次接口的请求是否成功
print(res.text)
print(res)
print(res.json()['root']['datas'][0]['msg'])
print(res.json()['root']['datas'][0]['success'])
# 通过断言校验本次测试是否成功
msg = True
assert msg == res.json()['root']['datas'][0]['success'], '断言失败'
