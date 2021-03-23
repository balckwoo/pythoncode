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
from common import handle_db
from common import handle_conf
import jsonpath
import requests


def random_number():
    """生成未注册手机号"""
    while True:
        phone = random.randint(13300000000, 13399999999)
        sql = "SELECT * FROM futureloan.member WHERE mobile_phone = {}".format(phone)
        res = handle_db.database_info.find_data(sql)
        if not res:
            return phone


def register_user(user_conf, pwd_conf, type=1):
    """注册普通用户账号"""
    url = handle_conf.Conf.get("env", "url") + "/member/register"
    headers = eval(handle_conf.Conf.get("env", "headers"))
    params = {"mobile_phone": random_number(),
              "pwd": "12345678",
              "type": type}
    method = "POST"
    requests.request(method=method, json=params, headers=headers, url=url)
    mobile = str(params["mobile_phone"])
    pwd = str(params["pwd"])
    handle_conf.Conf.write_data("test_data", user_conf, mobile)
    handle_conf.Conf.write_data("test_data", pwd_conf, pwd)
    return mobile, pwd


def login(mobile, pwd):
    """登录"""
    login_url = handle_conf.Conf.get("env", "url") + "/member/login"
    login_params = {"mobile_phone": mobile,
                    "pwd": pwd}
    headers = eval(handle_conf.Conf.get("env", "headers"))
    response = requests.request(url=login_url, method="post", json=login_params, headers=headers)
    res = response.json()
    # 提取token
    token = "Bearer" + " " + jsonpath.jsonpath(res, "$..token")[0]
    # 提取用户id
    member_id = jsonpath.jsonpath(res, "$..id")[0]
    return token, member_id


def recharge(token, member_id, amount=500000):
    """给该用户充值"""
    headers = eval(handle_conf.Conf.get("env", "headers"))
    headers["Authorization"] = token
    recharge_url = handle_conf.Conf.get("env", "url") + "/member/recharge"
    recharge_params = {"member_id": member_id, "amount": amount}
    requests.post(headers=headers, url=recharge_url, json=recharge_params)


def init_env_data():
    """注册普通用户"""
    user_info = register_user(user_conf="mobile", pwd_conf="pwd")
    """注册投资人账号"""
    invest_info = register_user(user_conf="invest_user", pwd_conf="invest_pwd")
    """admin账号"""
    admin_info = register_user(user_conf="admin_mobile", pwd_conf="admin_pwd", type=0)

    # 获取用户ID和token
    token, member_id = login(*user_info)
    recharge(token=token, member_id=member_id)
    recharge(token=token, member_id=member_id)

    # 投资人ID和token
    invest_token, invest_member_id = login(*invest_info)
    recharge(token=invest_token, member_id=invest_member_id)
    recharge(token=invest_token, member_id=invest_member_id)
