"""
========================================
# Author: Alem
# Date:2020/9/1 0001 Time:17:40
# Email: chengrichong@foxmail.com  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Two roads diverged in a wood,and I 
# I took the one less traveled by, 
# And that has made all the difference. 
=========================================

"""
import requests
from common import handle_conf, handle_db
import jsonpath

from tools import tools


def setup_login(cls):
    url = handle_conf.Conf.get("env", "url") + "/lifeAPI/login"
    headers = {"Content-Type": "application/json",
               "GL_DEVICE_ID": "test",
               "GL_CLIENT_ID": "test",
               "GL_CLIENT_VER": "test",
               "GL_TIMESTAMP": "test",
               "GL_REQ_SIGN": "{}".format(tools.get_login_sign())}

    params = {"username": handle_conf.Conf.get("test_data", "mobile"),
              "password": tools.find_pwd(),
              "deviceName": handle_conf.Conf.get("test_data", "deviceName"),
              "deviceVersion": handle_conf.Conf.get("test_data", "deviceVersion")}

    response = requests.post(url=url, headers=headers, json=params)
    res = response.json()

    # 用户登录token
    gl_token = res["data"]["token"]

    # 获取普通接口check_token
    cls.normal_header = {"Content-Type": "application/json",

                         "GL_DEVICE_ID": "test",
                         "GL_CLIENT_ID": "test",
                         "GL_CLIENT_VER": "test",
                         "GL_TIMESTAMP": "test",
                         "gl_token": "{}".format(gl_token),
                         "gl_req_sign": "{}".format(tools.get_sign_normal(gl_token))}

    check_token_url = handle_conf.Conf.get("env", "url") + "/lifeAPI/payPassword/getCheckToken"
    check_token_response = requests.get(url=check_token_url, headers=cls.normal_header).json()

    # print(type(check_token_response), check_token_response)
    cls.check_token_value = check_token_response["data"]


def submit_order_fixture(cls):
    """
    集采活动商品，预支付接口前置请求
    :param :
    :return:
    """
    submit_order_url = handle_conf.Conf.get("env", "url") + "/kstore/mobile/gl/order/submitOrder"
    cls.headers = tools.get_check_token()[1]
    # print(headers)
    submit_data = {
        "checkToken": "",
        "goodsInfoNum": 1,
        "goodsInfoId": int(tools.get_good_info_id(handle_conf.Conf.get("goods", "goods_info_item_no_huodong"))),
        "couponId": 0,
        "beanSwitch": "0",
        "shoppingAddrId": "",
        "generalizeId": "",
        "giveType": 1,
        "payId": 2,
        "userAgentNo": "",
        "userAgentType": "",
        "merchantNo": str(tools.get_merchant_no(handle_conf.Conf.get("goods", "goods_info_item_no_huodong"))),
        "thirdGoodsInfoId": "",
        "organCode": "",
        "payBeanAmount": 0,
        "payCashAmount": float(tools.get_payCashAmount(handle_conf.Conf.get("goods", "goods_info_item_no_huodong"))),
        "superMembersFlag": 0
    }

    submit_request = requests.post(url=submit_order_url, headers=cls.headers, json=submit_data).json()



def go_back_order():
    pass
