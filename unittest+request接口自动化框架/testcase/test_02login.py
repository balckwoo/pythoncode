"""
========================================
# Author: Alem
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
from common import handle_excel
from common import handle_path
from common import handle_logs
from common import handle_conf
from common import handle_data


@myddt.ddt
class TestLogin(unittest.TestCase):
    file_name = handle_excel.Test_case(os.path.join(handle_path.DATA_PATH, "test_case.xlsx"), "login")
    test_case = file_name.test_cases()

    @myddt.data(*test_case)
    def test_login(self, item):
        case_id = item["case_id"] + 1
        method = item["method"]
        url = handle_conf.Conf.get("env", "url") + item["url"]
        item["data"] = handle_data.replace_data(item["data"], TestLogin)
        params = eval(item["data"])
        expected = eval(item["expected"])
        headers = eval (handle_conf.Conf.get("env", "headers"))

        response = requests.request(method=method, url=url, json=params, headers=headers)
        res = response.json()
        print("预期结果：{}".format(expected))
        print("实际结果：{}".format(res))
        try:
            self.assertEqual(expected["code"], res["code"])
            self.assertEqual(expected["msg"], res["msg"])

        except AssertionError as e:
            handle_logs.log.error("用例{}未通过".format(item["title"]))
            handle_logs.log.exception(e)
            self.file_name.write_case(row=case_id, coulmn=8, value="失败")
            raise e

        else:
            handle_logs.log.info("用例{}通过".format(item["title"]))
            self.file_name.write_case(row=case_id, coulmn=8, value="成功")
