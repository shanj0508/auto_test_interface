import requests
import json

# requests.get('http://www.baidu.com')
# requests.post('http://dev.product.sysware.com.cn/eap/doLogin.action',
#               data={"loginName": "admin",
#                     "loginPassword": "Tfy53wCL11y2PiXm60k8i4stI69/8Va0PH30K9MNdv2eVA+mE0HDpNmjg7oQZS0Ji6YMaHbFr6laSPlw8BUpZd3b6tm+yKVyXMoLilZrsnuGrt2g2SeT3YNUOVtKcD4N/vyMJNEIxJRjFXoFzhnzbz0azfBd/+pmaroy6oaflqw="})

# get请求传递url参数
# url = 'http://www.baidu.com'
# params = {'key1': 'value1', 'key2': 'value2'}
# r = requests.get(url, params=params)
# print(r.url)  # http://www.baidu.com/?key2=value2&key1=value1

# 获取响应内容
# url = 'https://api.github.com/events'
# r = requests.get(url)
# print(r.text)
# print(type(r.text))
# json_data = r.json()
# print(json_data)
# print(r.json())
# print(type(r.json()))

# 通过json模块获取json响应内容
# url = 'https://api.github.com/events'
# r = requests.get(url)
# json_data = json.loads(r.text)
# print(json_data)
# print(type(json_data))

# post请求
# requests.post('http://dev.product.sysware.com.cn/eap/doLogin.action',
#               data={"loginName": "admin",
#                     "loginPassword": "Tfy53wCL11y2PiXm60k8i4stI69/8Va0PH30K9MNdv2eVA+mE0HDpNmjg7oQZS0Ji6YMaHbFr6laSPlw8BUpZd3b6tm+yKVyXMoLilZrsnuGrt2g2SeT3YNUOVtKcD4N/vyMJNEIxJRjFXoFzhnzbz0azfBd/+pmaroy6oaflqw="})
# url = 'http://httpbin.org/post'
# params = {'key1': 'value1', 'key2': 'value2'}
# r = requests.post(url, data=params)
# print(r.text)


# url = 'http://dev.product.sysware.com.cn/eap/doLogin.action'
# params = {"loginName": "admin",
#           "loginPassword": "Tfy53wCL11y2PiXm60k8i4stI69/8Va0PH30K9MNdv2eVA+mE0HDpNmjg7oQZS0Ji6YMaHbFr6laSPlw8BUpZd3b6tm+yKVyXMoLilZrsnuGrt2g2SeT3YNUOVtKcD4N/vyMJNEIxJRjFXoFzhnzbz0azfBd/+pmaroy6oaflqw="}
#
# params_json = json.dumps(params)
# print(type(params_json))  # <type 'str'>
# r = requests.post(url, data=params_json)
# # 用json接收参数
# # r = requests.post(url, json=params)
# print(r.text)
# print(r.status_code)  # 200

# 设置请求头
url = 'http://dev.product.sysware.com.cn/eap/doLogin.action'
params = {"loginName": "admin",
          "loginPassword": "Tfy53wCL11y2PiXm60k8i4stI69/8Va0PH30K9MNdv2eVA+mE0HDpNmjg7oQZS0Ji6YMaHbFr6laSPlw8BUpZd3b6tm+yKVyXMoLilZrsnuGrt2g2SeT3YNUOVtKcD4N/vyMJNEIxJRjFXoFzhnzbz0azfBd/+pmaroy6oaflqw="}

headers = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
}
r = requests.post(url, data=params, headers=headers)
print(r.text)
print(r.status_code)  # 200