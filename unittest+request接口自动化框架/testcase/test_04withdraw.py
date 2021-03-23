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
import jsonpath
import os
from common import myddt
import unittest
from common import handle_excel
from common import handle_path
from common import handle_logs
from common import handle_conf
from common import handle_db
from common import handle_data


@myddt.ddt
class Test_Withdraw(unittest.TestCase):
    file_name = handle_excel.Test_case(os.path.join(handle_path.DATA_PATH, "test_case.xlsx"), "withdraw")
    test_case = file_name.test_cases()

    @classmethod
    def setUpClass(cls):
        method = "post"
        url = handle_conf.Conf.get("env", "url") + "/member/login"
        params = {"mobile_phone": handle_conf.Conf.get("test_data", "mobile"),
                  "pwd": handle_conf.Conf.get("test_data", "pwd")}
        headers = eval(handle_conf.Conf.get("env", "headers"))
        response = requests.request(method=method, url=url, json=params, headers=headers)
        res = response.json()

        tk = jsonpath.jsonpath(res, "$..token")[0]
        cls.user_id = jsonpath.jsonpath(res, "$..id")[0]
        cls.token = "Bearer" + " " + tk

    @myddt.data(*test_case)
    def test_withdraw(self, item):
        url = handle_conf.Conf.get("env", "url") + item["url"]
        headers = eval(handle_conf.Conf.get("env", "headers"))
        headers["Authorization"] = self.token
        case_id = item["case_id"] + 1
        item["data"] = handle_data.replace_data(item["data"], Test_Withdraw)
        params = eval(item["data"])
        expected = eval(item['expected'])
        method = item["method"]
        if item["check_sql"]:
            old_amount = handle_db.database_info.find_data(item["check_sql"].format(self.uesr_id))
            old_money = old_amount[0]["leave_amount"]

        response = requests.request(method=method, url=url, headers=headers, json=params)
        res = response.json()
        print("预期结果：{}0".format(expected))
        print("实际结果：{}".format(res))
        try:
            self.assertEqual(expected["code"], res["code"])
            self.assertEqual(expected['msg'], res['msg'])
            if item["check_sql"]:
                new_amount = handle_db.database_info.find_data(item["check_sql"].format(self.uesr_id))
                new_money = new_amount[0]["leave_amount"]
                self.assertEqual(float(old_money - new_money), params["amount"])
        except AssertionError as e:
            handle_logs.log.error("失败，信息为{}".format(item["title"]))
            handle_logs.log.exception(e)
            self.file_name.write_case(row=case_id, coulmn=8, value="失败")
            raise e

        else:
            handle_logs.log.info("成功，记录信息为{}".format(item["title"]))
            self.file_name.write_case(row=case_id, coulmn=8, value="成功")
