"""
========================================
# Author: Alem
# Date:2020/9/1 0001 Time:16:53
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
import time
import rsa


# def random_number():
#     """生成未注册手机号"""
#     while True:
#         phone = random.randint(13300000000, 13399999999)
#         sql = "SELECT * FROM futureloan.member WHERE mobile_phone = {}".format(phone)
#         res = handle_db.database_info.find_data(sql)
#         if not res:
#             return phone
#
#
# def register_user(user_conf, pwd_conf, type=1):
#     """注册普通用户账号"""
#     url = handle_conf.Conf.get("env", "url") + "/member/register"
#     headers = eval(handle_conf.Conf.get("env", "headers"))
#     params = {"mobile_phone": random_number(),
#               "pwd": "12345678",
#               "type": type}
#     method = "POST"
#     requests.request(method=method, json=params, headers=headers, url=url)
#     mobile = str(params["mobile_phone"])
#     pwd = str(params["pwd"])
#     handle_conf.Conf.write_data("test_data", user_conf, mobile)
#     handle_conf.Conf.write_data("test_data", pwd_conf, pwd)
#     return mobile, pwd


# def login(mobile, pwd):
#     """登录"""
#     login_url = handle_conf.Conf.get("env", "url") + "/member/login"
#     login_params = {"mobile_phone": mobile,
#                     "pwd": pwd}
#     headers = eval(handle_conf.Conf.get("env", "headers"))
#     response = requests.request(url=login_url, method="post", json=login_params, headers=headers)
#     res = response.json()
#     # 提取token
#     token = "Bearer" + " " + jsonpath.jsonpath(res, "$..token")[0]
#     # 提取用户id
#     member_id = jsonpath.jsonpath(res, "$..id")[0]
#     return token, member_id


# def recharge(token, member_id, amount=500000):
#     """给该用户充值"""
#     headers = eval(handle_conf.Conf.get("env", "headers"))
#     headers["Authorization"] = token
#     recharge_url = handle_conf.Conf.get("env", "url") + "/member/recharge"
#     recharge_params = {"member_id": member_id, "amount": amount}
#     requests.post(headers=headers, url=recharge_url, json=recharge_params)


#
# def init_env_data():
#     """注册普通用户"""
#     user_info = register_user(user_conf="mobile", pwd_conf="pwd")
#     """注册投资人账号"""
#     invest_info = register_user(user_conf="invest_user", pwd_conf="invest_pwd")
#     """admin账号"""
#     admin_info = register_user(user_conf="admin_mobile", pwd_conf="admin_pwd", type=0)
#
#     # 获取用户ID和token
#     token, member_id = login(*user_info)
#     recharge(token=token, member_id=member_id)
#     recharge(token=token, member_id=member_id)
#
#     # 投资人ID和token
#     invest_token, invest_member_id = login(*invest_info)
#     recharge(token=invest_token, member_id=invest_member_id)
#     recharge(token=invest_token, member_id=invest_member_id)


def time_stamp():
    # time_stamp = '{0:%Y%m%d%H%M}'.format(datetime.datetime.now())
    time_s = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    return time_s


def get_login_sign():
    """

    :return: 生成登录用的sign
    """
    """https://uat-life.365gl.com/lifeAPI/getSign?text=testtesttesttest18603076567 000c85fc810df1f18b0172e5901e5a55"""

    url = "https://uat-life.365gl.com/lifeAPI/getSign?text=testtesttesttest" + "{}".format(
        handle_conf.Conf.get("test_data", "mobile")) + find_pwd()
    response = requests.request(method="get", url=url)
    res = response.json()
    login_sign = res["data"]
    return login_sign


# def login_get_token_userid():
#     url = handle_conf.Conf.get("env", "url") + "/login"
#     headers = {"Content-Type": "application/json",
#                "GL_DEVICE_ID": "test",
#                "GL_CLIENT_ID": "test",
#                "GL_CLIENT_VER": "test",
#                "GL_TIMESTAMP": "test",
#                "GL_REQ_SIGN": "{}".format(get_login_sign())}
#
#     params = {"username": handle_conf.Conf.get("test_data", "mobile"),
#               "password": find_pwd(),
#               "deviceName": handle_conf.Conf.get("test_data", "deviceName"),
#               "deviceVersion": handle_conf.Conf.get("test_data", "deviceVersion")}
#     response = requests.post(url=url, headers=headers, json=params)
#     res = response.json()
#     gl_userId = res["data"]["userId"]
#     gl_token = res["data"]["token"]
#     return gl_token, gl_userId


def find_pwd():
    """

    :return:查找配置文件手机号的MD5密码,返回密码
    """
    f_pwd = handle_db.database_info.find_data(
        'SELECT `password` from member_data.`user` WHERE mobile_phone = "{}"'.format(
            handle_conf.Conf.get("test_data", "mobile")))
    pwd = f_pwd[0]["password"]

    return pwd


def get_login_sign_from_db(mobile):
    """

    :param mobile: 传入手机号到数据库查找md5加密后的密码
    :return: 数据库未查到该手机号数据，则返回一条只有手机号的sign，否则返回正确的sign
    """

    f_pwd = handle_db.database_info.find_data(
        'SELECT `password` from member_data.`user` WHERE mobile_phone = "{}"'.format(
            mobile))
    if len(f_pwd) == 0:
        url = "https://uat-life.365gl.com/lifeAPI/getSign?text=testtesttesttest" + "{}".format(
            mobile) + "f58ac543d4a76afe6fb9e3dbd80eedeb"
        res = requests.request(method="get", url=url).json()
        login_sign = res["data"]
        return login_sign, len(f_pwd)

    else:
        pwd = f_pwd[0]["password"]
        url = "https://uat-life.365gl.com/lifeAPI/getSign?text=testtesttesttest" + "{}".format(mobile) + pwd
        res_1 = requests.request(method="get", url=url).json()
        login_sign_true_pwd = res_1["data"]
        return login_sign_true_pwd, pwd


def get_error_pwd_sign(mobile, error_pwd):
    """

    :param mobile: 登录账号
    :param error_pwd: 错误的登录密码
    :return: 返回错误登录密码加密后的sign
    """
    # 获取错误密码的sign
    url = "https://uat-life.365gl.com/lifeAPI/getSign?text=testtesttesttest" + "{}".format(
        mobile) + "{}".format(error_pwd)
    res_1 = requests.get(url=url).json()
    error_pwd_sign = res_1["data"]
    return error_pwd_sign


def get_sign_normal(token):
    """
    通过用户登录token，获取普通接口的sign
    :param token: 用户登录返回的token
    :return:
    """

    url = "http://10.252.252.103:18082/lifeAPI/getSign?text=" + "{}".format(token
                                                                            ) + "testtesttesttest"
    response = requests.request(method="get", url=url)
    res = response.json()
    sign_2 = res["data"]
    return sign_2


def get_check_token():
    """
    账号登录获取sign和用户token,只有纯霸王豆支付时需要在参数内代入check_token
    :return:
    """

    url = handle_conf.Conf.get("env", "url") + "/lifeAPI/login"
    headers = {"Content-Type": "application/json",
               "GL_DEVICE_ID": "test",
               "GL_CLIENT_ID": "test",
               "GL_CLIENT_VER": "test",
               "GL_TIMESTAMP": "test",
               "GL_REQ_SIGN": "{}".format(get_login_sign())}

    params = {"username": handle_conf.Conf.get("test_data", "mobile"),
              "password": find_pwd(),
              "deviceName": handle_conf.Conf.get("test_data", "deviceName"),
              "deviceVersion": handle_conf.Conf.get("test_data", "deviceVersion")}

    response = requests.post(url=url, headers=headers, json=params)
    res = response.json()

    # 用户登录token
    gl_token = res["data"]["token"]

    # 获取普通接口check_token
    check_token_header = {"Content-Type": "application/json",
                          "GL_DEVICE_ID": "test",
                          "GL_CLIENT_ID": "test",
                          "GL_CLIENT_VER": "test",
                          "GL_TIMESTAMP": "test",
                          "gl_token": "{}".format(gl_token),
                          "gl_req_sign": "{}".format(get_sign_normal(gl_token))}

    check_token_url = handle_conf.Conf.get("env", "url") + "/lifeAPI/payPassword/getCheckToken"
    check_token_response = requests.get(url=check_token_url, headers=check_token_header).json()
    # print(check_token_response)
    check_token_value = check_token_response["data"]
    return check_token_value, check_token_header


def get_good_info_id(goods_info_item_no):
    """
    传入货号，查找货品ID
    :param goods_info_item_no:
    :return:
    """
    find_sql = handle_db.database_info.find_data(
        "SELECT goods_info_id FROM kstore_data.gl_goods_info WHERE goods_info_item_no = '{}'".format(
            goods_info_item_no))
    goods_info_id = find_sql[0]["goods_info_id"]

    return goods_info_id


def get_merchant_no(goods_info_item_no):
    """
    查询商户号，传入商品编号
    :param goods_info_item_no:
    :return:
    """
    goods_info_id = get_good_info_id(goods_info_item_no)
    goods_id = handle_db.database_info.find_data(
        "SELECT goods_id FROM kstore_data.gl_goods_info WHERE goods_info_id = '{}'".format(goods_info_id
                                                                                           ))
    goods_id_value = goods_id[0]["goods_id"]
    binding_third_no = handle_db.database_info.find_data(
        "SELECT binding_third_no FROM kstore_data.gl_goods WHERE goods_id = '{}'".format(goods_id_value))
    binding_third_no_value = binding_third_no[0]["binding_third_no"]
    # print(binding_third_no_value)

    return binding_third_no_value


def get_payCashAmount(goods_info_item_no):
    """
    查询订单支付价格
    :param goods_info_item_no:
    :return:
    """
    price = "SELECT goods_info_prefer_price FROM kstore_data.gl_goods_info WHERE goods_info_item_no = '{}'".format(
        goods_info_item_no)
    goods_info_prefer_price = handle_db.database_info.find_data(price)[0]["goods_info_prefer_price"]
    return goods_info_prefer_price


def find_order_id():
    """
    查找活动商品的订单ID
    :return:
    """
    sql = 'SELECT order_id FROM kstore_data.gl_order WHERE merchant_no = "{}" and customer_mobile = "{}" ORDER BY create_time DESC'.format(
        get_merchant_no(handle_conf.Conf.get("goods", "goods_info_item_no_huodong")),
        handle_conf.Conf.get("test_data", "mobile"))
    order_id = handle_db.database_info.find_data(sql)[0]["order_id"]
    return order_id


if __name__ == '__main__':
    find_order_id()
