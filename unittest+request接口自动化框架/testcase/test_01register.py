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
import random
import requests
import os
from common import myddt
import unittest
from common import handle_excel
from common import handle_path
from common import handle_logs
from common import handle_conf
from common import handle_db


@myddt.ddt
class Test_Register(unittest.TestCase):
    file_name = handle_excel.Test_case(os.path.join(handle_path.DATA_PATH, "test_case.xlsx"), "register")
    test_case = file_name.test_cases()

    @myddt.data(*test_case)
    def test_register(self, item):
        url = handle_conf.Conf.get("env", "url") + item["url"]
        headers = eval(handle_conf.Conf.get("env", "headers"))
        case_id = item["case_id"] + 1
        method = item["method"]
        if "#mobile#" in item["data"]:
            phone = self.random_phone()
            item["data"] = item["data"].replace("#mobile#", str(phone))
        params = eval(item["data"])
        expected = eval(item["expected"])

        response = requests.request(url=url, headers=headers, method=method, json=params)
        res = response.json()
        print("预期结果：{}".format(expected))
        print("实际结果：{}".format(res))

        try:
            self.assertEqual(expected["code"], res["code"])
            self.assertEqual(expected["msg"], res["msg"])
            if item["check_sql"]:
                check_data = handle_db.database_info.find_data(item["check_sql"].format(phone))
                self.assertTrue(check_data)
        except AssertionError as e:
            handle_logs.log.error("失败，信息为{}".format(item['title']))
            handle_logs.log.exception(e)
            self.file_name.write_case(row=case_id, coulmn=8, value="失败")
            raise e

        else:
            handle_logs.log.info("成功，信息为{}".format(item["title"]))
            self.file_name.write_case(row=case_id, coulmn=8, value="成功")

    @staticmethod
    def random_phone():
        while True:
            phone = random.randint(13300000000, 13399999999)
            sql = "SELECT mobile_phone FROM futureloan.member where mobile_phone = {}".format(phone)
            res = handle_db.database_info.find_data(sql)
            if not res:
                return phone
