from aip_key.api import ApiDemo
import unittest
from ddt import ddt, file_data


@ddt
class CaseDemo(unittest.TestCase):
    @classmethod
    def setUp(self) -> None:
        self.ad = ApiDemo()

    @file_data('../data/user.yaml')
    def test_01_login(self, data, resflag):
        # 请求数据的准备
        url = 'http://dev.product.sysware.com.cn/eap/doLogin.action'
        # 模拟请求的下发
        res = self.ad.do_post(url=url, data=data)
        # 解析响应结果，判断本次接口的请求是否成功
        # print(res.text)
        # print(res)
        # 通过断言校验本次测试是否成功
        self.assertEqual(resflag, res.json()['root']['datas'][0]['success'], '断言失败')

    def test_02_login(self):
        # 请求数据的准备
        url = 'http://dev.product.sysware.com.cn/eap/'
        # 模拟请求的下发
        res = self.ad.do_get(url=url)
        # 解析响应结果，判断本次接口的请求是否成功
        # print(res.text)
        print(res.status_code)
        # 通过断言校验本次测试是否成功
        msg = 200
        self.assertEqual(msg, res.status_code, '断言失败')


if __name__ == '__main__':
    unittest.main()
