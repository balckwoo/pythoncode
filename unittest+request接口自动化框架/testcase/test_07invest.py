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
class Test_Invest(unittest.TestCase):
    case_file = handle_excel.Test_case(os.path.join(handle_path.DATA_PATH, "test_case.xlsx"), "invest")
    test_case = case_file.test_cases()

    @classmethod
    def setUpClass(cls):
        fixture.setup_login_admin(cls)
        fixture.setup_login(cls)
        fixture.setup_login_invest_user(cls)
        fixture.setup_add(cls)

        aduit_url = handle_conf.Conf.get("env", "url") + "/loan/audit"
        headers = eval(handle_conf.Conf.get("env", "headers"))
        headers["Authorization"] = cls.admin_token
        params = {"loan_id": cls.loan_id, "approved_or_not": True}
        response = requests.patch(url=aduit_url, headers=headers, json=params)
        # res = response.json()

    @myddt.data(*test_case)
    def test_invest(self, item):
        url = handle_conf.Conf.get("env", "url") + item["url"]
        headers = eval(handle_conf.Conf.get('env', 'headers'))
        headers["Authorization"] = self.invest_token
        item["data"] = handle_data.replace_data(item["data"], Test_Invest)
        params = eval(item["data"])
        method = item['method']
        expected = eval(item["expected"])
        case_id = item["case_id "] + 1
        if item["check_sql"]:
            """查询原始表该投资用户在表内的投资记录"""
            sql1 = "SELECT * FROM futureloan.invest WHERE member_id ={} and loan_id ={}".format(self.invest_id,
                                                                                                self.loan_id)
            """余额"""
            sql2 = "SELECT * FROM futureloan.member WHERE member_id ={}".format(self.invest_id)
            """流水记录"""
            sql3 = "SELECT * FROM futureloan.financelog WHERE pay_member_id = {}".format(self.invest_id)

            f_invest = len(handle_db.database_info.find_data(sql1))
            f_amount = handle_db.database_info.find_data(sql2)[0]["amount"]
            f_financelog = len(handle_db.database_info.find_data(sql3))
        response = requests.request(method=method, url=url, headers=headers, json=params)
        res = response.json()

        print("预期结果：{}0".format(expected))
        print("实际结果：{}".format(res))
        try:
            self.assertEqual(expected['code'], res["code"])
            self.assertEqual(expected['msg'], res['msg'])
            if item["check_sql"]:
                sql1 = "SELECT * FROM futureloan.invest WHERE member_id ={} and loan_id ={}".format(self.invest_id,
                                                                                                    self.loan_id)
                sql2 = "SELECT * FROM futureloan.member WHERE member_id ={}".format(self.invest_id)
                sql3 = "SELECT * FROM futureloan.financelog WHERE pay_member_id = {}".format(self.invest_id)

                s_invest = len(handle_db.database_info.find_data(sql1))
                s_amount = handle_db.database_info.find_data(sql2)[0]["amount"]
                s_financelog = len(handle_db.database_info.find_data(sql3))

                self.assertEqual(s_invest - f_invest, 1)
                self.assertEqual(s_amount - f_amount, params["amount"])
                self.assertEqual(s_financelog - f_financelog, 1)

        except AssertionError as e:
            handle_logs.log.error("失败，记录信息为{}".format(item['title']))
            handle_logs.log.exception(e)
            self.case_file.write_case(row=case_id, coulmn=8, value="失败")

        else:
            handle_logs.log.info("成功，记录信息为{}".format(item['title']))
            self.case_file.write_case(row=case_id, coulmn=8, value="成功")
