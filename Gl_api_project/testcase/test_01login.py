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
from common import handle_excel, handle_path, handle_logs, handle_conf, handle_data
from tools import tools


@myddt.ddt
class TestLogin(unittest.TestCase):
    case_file = handle_excel.Test_case(os.path.join(handle_path.DATA_PATH, "GL_test_case.xlsx"), "login")
    test_case = case_file.test_cases()

    @myddt.data(*test_case)
    def test_login_pass(self, items):
        case_id = items["case_id"]
        if items["title"] != "密码错误":
            login_header = {"Content-Type": "application/json",
                            "GL_DEVICE_ID": "test",
                            "GL_CLIENT_ID": "test",
                            "GL_CLIENT_VER": "test",
                            "GL_TIMESTAMP": "test",
                            "GL_REQ_SIGN": "{}".format(
                                tools.get_login_sign_from_db(eval(self.test_case[case_id - 1]["data"])["username"])[0])}
        else:
            login_header = {"Content-Type": "application/json",
                            "GL_DEVICE_ID": "test",
                            "GL_CLIENT_ID": "test",
                            "GL_CLIENT_VER": "test",
                            "GL_TIMESTAMP": "test",
                            "GL_REQ_SIGN": "{}".format(
                                tools.get_error_pwd_sign(mobile=eval(self.test_case[case_id - 1]["data"])["username"],
                                                         error_pwd=eval((self.test_case[case_id - 1])["data"])["password"]
                                                         ))}
        url = handle_conf.Conf.get("env", "url") + items["url"]
        # items["data"] = handle_data.replace_data(items["data"], TestLogin).format(
        #     self.test_case[case_id - 1]["data"]["username"])
        params = eval(items["data"])
        expected = eval(items["expected"])

        res = requests.request(url=url, method=items["method"], json=params, headers=login_header).json()

        try:
            self.assertEqual(expected["result"], res["result"])
            self.assertEqual(expected["description"], res["description"])
        except AssertionError as e:
            handle_logs.log.error("用例{}未通过".format(items["title"]))
            handle_logs.log.exception(e)
            self.case_file.write_case(row=case_id + 1, coulmn=8, value="失败")
            raise e

        else:
            handle_logs.log.info("用例{}通过".format(items["title"]))
            self.case_file.write_case(row=case_id + 1, coulmn=8, value="成功")
