"""
========================================
# Author: Alem
# Date:2021/3/11 0011  
# Time:下午 12:01
# Email: chengrichong@foxmail.com  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Two roads diverged in a wood,and I 
# I took the one less traveled by, 
# And that has made all the difference. 
=========================================

"""
import requests
import os
from common import myddt
import unittest
from common import handle_excel, handle_path, handle_logs, handle_conf
from tools import tools
from testcase import fixture


@myddt.ddt
class TestLogin(unittest.TestCase):
    case_file = handle_excel.Test_case(os.path.join(handle_path.DATA_PATH, "GL_test_case.xlsx"), "order_bwd_baoping")
    test_case = case_file.test_cases()

    @classmethod
    def setUpClass(cls):
        fixture.setup_login(cls)

    @myddt.data(*test_case)
    # 纯霸王豆支付,线上爆品
    def test_order_pay_type8(self, items):
        url = handle_conf.Conf.get('env', 'url') + items["url"]
        method = items["method"]
        headers = self.normal_header
        case_id = items["case_id"] + 1
        check_token = self.check_token_value
        # 将excel内的替换参数进行参数化替换；
        if "#checktoken#" in items["data"]:
            items["data"] = items["data"].replace("#checktoken#", check_token)
            if "#goodsInfoId#" in items["data"]:
                items["data"] = items["data"].replace("#goodsInfoId#", str(tools.get_good_info_id(
                    handle_conf.Conf.get("goods", "goods_info_item_no_bwd_baopin"))))
                if "#payId#" in items["data"]:
                    items["data"] = items["data"].replace("#payId#", handle_conf.Conf.get("goods", "payId_bwd_baopin"))
                    if "#merchantNo#" in items["data"]:
                        items["data"] = items["data"].replace("#merchantNo#", str(
                            tools.get_merchant_no(handle_conf.Conf.get("goods", "goods_info_item_no_bwd_baopin"))))

        params = eval(items["data"])
        expected = eval(items["expected"])
        res = requests.request(url=url, json=params, headers=headers, method=method).json()

        try:
            self.assertEqual(expected["status"], res["status"])
            self.assertEqual(expected["code"], res["code"])
            self.assertEqual(expected["message"], res["message"])
        except AssertionError as e:
            handle_logs.log.error("用例执行失败，记录信息为-----{}-----".format(items['title']))
            handle_logs.log.error(e)
            self.case_file.write_case(row=case_id, coulmn=8, value="失败")
            raise e
        else:
            handle_logs.log.info("用例执行成功，记录信息为-----{}-----".format(items['title']))
            self.case_file.write_case(row=case_id, coulmn=8, value="成功")



