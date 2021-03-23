"""
========================================
# Author: Alem
# Date:2020/9/3 0003 Time:17:29
# Email: chengrichong@foxmail.com  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Two roads diverged in a wood,and I 
# I took the one less traveled by, 
# And that has made all the difference. 
=========================================

"""
import unittest
import unittestreport
from common import handle_path
from common import handle_conf
from tools import tools

# tools.init_env_data()

suite = unittest.TestSuite()
loader = unittest.TestLoader()

suite.addTest(loader.discover(handle_path.CASE_PATH))
runner = unittestreport.TestRunner(suite,
                                   filename=handle_conf.Conf.get("report", "report_name"),
                                   report_dir=handle_path.REPORT_PATH,
                                   title='test_report',
                                   tester='Alem',
                                   desc="Alem_project_test_report")

runner.run()
