#修改折扣测试用例
import unittest,time
from common import login

class updateDiscount_class(unittest.TestCase):
    def setUp(self):
        #调用驱动
        self.driver = login.get_driver()

    def tearDown(self):
        self.driver.quit()

    def test_updateDiscount(self):
        driver=self.driver
        #driver.find_element_by_xpath('//android.widget.Button[@text="我知道了 "]').click()
        time.sleep(5)
        driver.find_element_by_xpath('//android.view.View[@text="我的"]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//android.view.View[@text=">"]').click()
        driver.find_element_by_xpath('//android.widget.EditText[@text="9折输入90，8.5折输入85"]').send_keys("82")
        driver.find_element_by_xpath('//android.widget.EditText[@text="请输入商户账号登录密码"]').send_keys("a12345678")
        time.sleep(1)
        driver.find_element_by_xpath('//android.widget.Button[@text="提交申请"]').click()
        print("提交申请")
        try:
            driver.find_element_by_xpath('//android.widget.Button[@text="我知道了 "]').click()
            time.sleep(2)
            print("点击我知道了")
        except:
            pass
            print("修改成功")

