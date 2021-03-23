
from GeiLeB.test_case import login_test,updateDiscount,updatePicture
# 统一入口运行
import unittest  # 单元测试框架：组织与管理测试用例
import HTMLReport  # 运行测试并生成报告


# 创建一个总的测试套件
suite = unittest.TestSuite()
# 将各个模块的测试套件加入到总的测试套件中
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(login_test.login_test_class))
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(updateDiscount.updateDiscount_class))
#suite.addTest(unittest.TestLoader().loadTestsFromTestCase(updatePicture.updatePicture_class))


# 运行测试套件，并生成报告
HTMLReport.TestRunner(
    title="XX项目自动化测试报告",
    description="XX项目测试报告，本次测试覆盖XX模块",
    thread_count=1
).run(suite)
