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
from testcase import fixture


@myddt.ddt
class Test_Aduit(unittest.TestCase):
    case_file = handle_excel.Test_case(os.path.join(handle_path.DATA_PATH, "test_case.xlsx"), "audit")
    test_case = case_file.test_cases()

    @classmethod
    def setUpClass(cls):
        fixture.setup_login(cls)
        fixture.setup_login_admin(cls)

    def setUp(self):
        url = handle_conf.Conf.get("env", "url") + "/loan/add"
        headers = eval(handle_conf.Conf.get("env", "headers"))
        headers["Authorization"] = self.token
        params = {"member_id": self.user_id,
                  "title": "fix_title",
                  "amount": 3000,
                  "loan_rate": 12.0,
                  "loan_term": 3,
                  "loan_date_type": 1,
                  "bidding_days": 5}
        response = requests.post(url=url, headers=headers, json=params)
        res = response.json()
        loan_id = jsonpath.jsonpath(res, "$..id")[0]
        Test_Aduit.loan_id = loan_id

    @myddt.data(*test_case)
    def test_audit(self, item):
        url = os.path.join(handle_conf.Conf.get("env", "url")) + item["url"]
        headers = eval(handle_conf.Conf.get("env", "headers"))
        headers["Authorization"] = self.admin_token
        method = item["method"]
        item["data"] = handle_data.replace_data(item['data'], Test_Aduit)
        params = eval(item["data"])
        expected = eval(item["expected"])
        case_id = item["case_id"] + 1

        response = requests.request(method=method, url=url, headers=headers, json=params)
        res = response.json()
        print("预期结果：{}0".format(expected))
        print("实际结果：{}".format(res))
        try:
            self.assertEqual(res["code"], expected["code"])
            self.assertEqual(res["msg"], expected["msg"])
            if item["check_sql"]:
                status = handle_db.database_info.find_data(item["check_sql"].format(params["loan_id"]))[0]
                self.assertEqual(expected["status"], status["status"])
        except AssertionError as e:
            handle_logs.log.error("未通过，记录信息为{}".format(item["title"]))
            handle_logs.log.exception(e)
            self.case_file.write_case(row=case_id, coulmn=8, value="失败")
            raise e

        else:
            handle_logs.log.info("通过，记录信息为{}".format(item["title"]))
            self.case_file.write_case(row=case_id, coulmn=8, value="成功")
