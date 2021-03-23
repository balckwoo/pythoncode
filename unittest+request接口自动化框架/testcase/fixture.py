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
from common import handle_conf
import jsonpath

from appium.webdriver import Remote
from selenium.webdriver import Chrome


def setup_login(cls):
    url = handle_conf.Conf.get("env", "url") + "/member/login"
    headers = eval(handle_conf.Conf.get("env", "headers"))
    params = {"mobile_phone": handle_conf.Conf.get("test_data", "mobile"), "pwd": handle_conf.Conf.get("test_data", "pwd")}

    response = requests.post(url=url, headers=headers, json=params)
    res = response.json()
    token = jsonpath.jsonpath(res, "$..token")[0]
    cls.user_id = jsonpath.jsonpath(res, "$..id")[0]
    cls.token = "Bearer" + " " + token


def setup_login_admin(cls):
    url = handle_conf.Conf.get("env", "url") + "/member/login"
    headers = eval(handle_conf.Conf.get("env", "headers"))
    params = {"mobile_phone": handle_conf.Conf.get("test_data", "admin_mobile"),
              "pwd": handle_conf.Conf.get("test_data", "admin_pwd")}
    response = requests.post(url=url, headers=headers, json=params)
    res = response.json()
    cls.admin_token = "Bearer" + " " + jsonpath.jsonpath(res, "$..token")[0]
    cls.admin_id = jsonpath.jsonpath(res, "$..id")[0]


def setup_login_invest_user(cls):
    url = handle_conf.Conf.get("env", "url") + "/member/login"
    headers = eval(handle_conf.Conf.get("env", "headers"))
    params = {"mobile_phone": handle_conf.Conf.get("test_data", "invest_mobile"),
              "pwd": handle_conf.Conf.get("test_data", "invest_pwd")}
    response = requests.post(url=url, headers=headers, json=params)
    res = response.json()
    cls.invest_token = "Bearer" + " " + jsonpath.jsonpath(res, "$..token")[0]
    cls.invest_id = jsonpath.jsonpath(res, "$..id")[0]


def setup_add(cls):
    url = handle_conf.Conf.get("env", "url") + "/loan/add"
    headers = eval(handle_conf.Conf.get("env" , "headers"))
    headers["Authorization"] = cls.token
    params = {"member_id": cls.user_id,
              "title": "fix_title",
              "amount": 10000,
              "loan_rate": 12.0,
              "loan_term": 3,
              "loan_date_type": 1,
              "bidding_days": 5}
    response = requests.post(url=url, headers=headers, json=params)
    res = response.json()
    cls.loan_id = jsonpath.jsonpath(res, "$..id")[0]





