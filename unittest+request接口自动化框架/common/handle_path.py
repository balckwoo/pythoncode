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

import os

# 项目根路径
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_PATH)

# 用例路径
CASE_PATH = os.path.join(BASE_PATH, "testcase")

# 日志路径
LOG_PATH = os.path.join(BASE_PATH, "logs")

# 测试报告路径
REPORT_PATH = os.path.join(BASE_PATH, "report")

# 公共模块工具路径
COMMON_PATH = os.path.join(BASE_PATH, "common")

# 测试用例文件路径
DATA_PATH = os.path.join(BASE_PATH, "data")

# 配置文件路径
CONF_PATH = os.path.join(BASE_PATH, "conf")
