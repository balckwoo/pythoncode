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
import re
from common.handle_conf import Conf


def replace_data(data, cls):
    """替换用例参数"""
    while re.search("#(.+?)#", data):
        item = re.search("#(.+?)#", data)
        # 需要替换的数据
        rep_data = item.group()
        # 要替换的属性
        key = item.group(1)
        try:
            value = Conf.get("test_data", key)
        except:
            value = getattr(cls, key)
        data = data.replace(rep_data, str(value))
    return data


