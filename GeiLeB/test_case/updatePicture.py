import unittest,time
from common import login

class updatePicture_class(unittest.TestCase):
    def setUp(self):
        self.driver=login.get_driver("com.gl365.android.merchant",".MainActivity")

    def tearDown(self):
        if self.driver:
            self.driver.quit()

    def test_updatePicture(self):
        driver=self.driver
        time.sleep(3)
        print("进进进")
        #driver.find_element_by_xpath('//android.widget.Button[@text="我知道了 "]').click()
        driver.find_element_by_xpath('//android.view.View[@text="我的"]').click()
        print("我的")
        driver.find_element_by_xpath('//android.view.View[@text="商家基本信息"]').click()
        driver.find_element_by_xpath('//android.view.View[@text="编辑"]').click()
        driver.find_element_by_xpath('//android.view.View[@index="6"]').click()
        time.sleep(3)
        driver.find_element_by_xpath('//android.widget.Button[@text="本地相册选取"]').click()
        driver.find_element_by_xpath('//com.sec.samsung.gallery.glview.composeView.ThumbObject[@index="1"]').click()
        driver.find_element_by_xpath('//android.view.View[@text="保存"]').click()
        driver.find_element_by_xpath('//android.widget.Button[@text="我知道了 "]').click()

