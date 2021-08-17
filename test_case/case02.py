from aip_key.api import ApiDemo
import unittest


class CaseDemo(unittest.TestCase):
    def test_01_login(self):
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
        # 通过断言校验本次测试是否成功
        msg = True
        self.assertEqual(msg, res.json()['root']['datas'][0]['success'], '断言失败')

    def test_02_login(self):
        ad = ApiDemo()

        # 请求数据的准备
        url = 'http://dev.product.sysware.com.cn/eap/doLogin.action'
        data = {
            'loginName': 'admin',
            'loginPassword': '123456'
        }

        # 模拟请求的下发
        res = ad.do_post(url=url, data=data)

        # 解析响应结果，判断本次接口的请求是否成功
        print(res.text)
        print(res)
        # 通过断言校验本次测试是否成功
        msg = "用户名或密码错误！"
        self.assertEqual(msg, res.json()['root']['datas'][0]['msg'], '断言失败')


if __name__ == '__main__':
    unittest.main()
