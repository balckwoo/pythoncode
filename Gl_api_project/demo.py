"""
========================================
# Author: Alem
# Date:2021/3/11 0011  
# Time:下午 6:06
# Email: chengrichong@foxmail.com  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Two roads diverged in a wood,and I 
# I took the one less traveled by, 
# And that has made all the difference. 
=========================================

"""
import os

import jsonpath

from common import handle_db, handle_conf, handle_excel, handle_path
import requests
from common import myddt
from tools import tools
from testcase import fixture

# case_file = handle_excel.Test_case(os.path.join(handle_path.DATA_PATH, "GL_test_case.xlsx"), "order")
# test_case = case_file.test_cases()
# res = test_case[0]


# # 纯霸王豆支付
# def test_order_pay_type8():
#     url = "https://uat-life.365gl.com/kstore/mobile/gl/order/submitOrder"
#     check_token, headers = tools.get_check_token()
#
#     params = {
#         "checkToken": "{}".format(check_token),
#         "goodsInfoNum": 1,
#         "goodsInfoId": 13442,
#         "couponId": 0,
#         "beanSwitch": "1",
#         "shoppingAddrId": 42517,
#         "generalizeId": "",
#         "giveType": 1,
#         "payId": 8,
#         "userAgentNo": "",
#         "userAgentType": "",
#         "merchantNo": "",
#         "thirdGoodsInfoId": "",
#         "organCode": "",
#         "payBeanAmount": "11",
#         "payCashAmount": 1,
#         "superMembersFlag": 0
#     }
#     res = requests.post(url=url, json=params, headers=headers)
#     print(res)
#
#
# def get_login_sign():
#     """
#
#     :return: 生成登录用的sign
#     """
#     """https://uat-life.365gl.com/lifeAPI/getSign?text=testtesttesttest18603076567 000c85fc810df1f18b0172e5901e5a55"""
#
#     url = "https://uat-life.365gl.com/lifeAPI/getSign?text=testtesttesttest" + "{}".format(
#         handle_conf.Conf.get("test_data", "mobile")) + tools.find_pwd()
#     response = requests.request(method="get", url=url)
#     print(response, type(response))
#
#     res = response.json()
#     login_sign = res["data"]
#     return login_sign


# str = '            Hello world                '
# str_1 = str.strip()
# print(str)
# print(str_1)

#
# str = "今天是星期{},今天是星期{}今天是星期{}今天是星期{}".format(7, 4, 5, 9)
# print(str)

# 
# str = "2345"
# str_1 = float(str)
# print(type(str_1))
# print(str_1)

#
# str = (1,2,5,7,9,4,"a","o",4)
# print(str[-1])
# print (str[1:5])

# print(type(str))
# print(str)

# list1 = ['physics', 'chemistry', 1997, 2000,666,444]
#
# list1.append("string")
# # list1.extend()
# print(list1)

# data = [1, 2, 3, 4, 5]
# del (data[3])
# print(data)

# data = {"a": 1, "b": 2, "c": 3, "d": 4}
# res = data.get("c")
# print(res)

# data = {"a": 1, "b": 2, "c": 3, "d": 4}
# data.update({"a":999,"zzz":11})
# print(data)


# data = {"a": 1, "b": 2, "c": 3, "d": 4}
# res = data.keys()
# print(res)

# print(dict["str"])

# for k,v in dict.items():
#     print(k,v)
# print(res)
# print(res[1])

# json_1 = "{'key':'value'}"
#
# print(dict,json_1)


submit_order_url = handle_conf.Conf.get("env", "url") + "/kstore/mobile/gl/order/submitOrder"
headers = tools.get_check_token()[1]
print(headers)
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

submit_request = requests.post(url=submit_order_url, headers=headers, json=submit_data).json()
print(submit_request)
