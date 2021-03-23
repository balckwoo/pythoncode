"""
========================================
# Author: Alem
# Date:2021/3/16 0016  
# Time:下午 2:29
# Email: chengrichong@foxmail.com  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Two roads diverged in a wood,and I 
# I took the one less traveled by, 
# And that has made all the difference. 
=========================================

"""


class ApiExplain:
    # 订单接口
    submitOrder_api = {
        # 验证check_token
        "checkToken": "e84e0ee97dbd4a619ffc8e63ffefa96d",
        # 货品数量/购买数量
        "goodsInfoNum": 1,
        # 货品ＩＤ
        "goodsInfoId": 13442,
        # 优惠劵编号
        "couponId": 0,
        # 乐豆开关，0为不使用，1为使用乐豆
        "beanSwitch": "1",
        # 收货地址ID
        "shoppingAddrId": 42517,
        # 推广id
        "generalizeId": "",
        # 0:赠送订单1:自收订单
        "giveType": 1,
        # 支付方式:1 微信支付,2 微信+乐豆支付,3 支付宝支付,4支付宝+乐豆支付,5 乐豆支付,6 优惠券抵扣,7充值卡支付,8霸王豆支付,9 微信+乐豆支付+霸王豆,10支付宝+乐豆支付+霸王豆',
        "payId": 8,
        # 发展关系
        "userAgentNo": "",
        # 发展类型
        "userAgentType": "",
        # 商户号
        "merchantNo": "",
        # 第三方货品ID
        "thirdGoodsInfoId": "",
        # 机构编码
        "organCode": "",
        # 支付乐豆金额
        "payBeanAmount": "11",
        # 支付现金金额
        "payCashAmount": 1,
        # 是否是超级会员商品 0：否 1：是
        "superMembersFlag": 0
    }
