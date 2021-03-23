import unittest ,time
import GeiLeB.common.login

class login_test_class(unittest.TestCase):
    def setUp(self):
        #调用驱动
        self.driver = GeiLeB.common.login.get_driver()

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        driver=self.driver
        time.sleep(8)
        try:
            #driver.find_element_by_xpath('//android.widget.Button[@text="我知道了 "]').click()
            time.sleep(2)
            driver.find_element_by_xpath('//android.view.View[@text="我的"]').click()
            time.sleep(1)
            driver.find_element_by_xpath('//android.view.View[@text="设置"]').click()
            time.sleep(2)
            driver.find_element_by_xpath('//android.widget.Button[@text="退出登录"]').click()
            time.sleep(3)

            print("退出")
            #try:
            driver.find_element_by_xpath('//android.widget.Button[@text="确定 "]').click()
            time.sleep(8)
            #except Exception as e:
                #pass
        except:
            pass
       #点击总是允许按钮
        #driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
        #print("总是允许")
        #time.sleep(1)
        #driver.swipe(0.9,0.5,0.1,0.5,1000)
        #time.sleep(1)
        #driver.swipe(0.9,0.5,0.1,0.5,1000)
        #time.sleep(1)
        #driver.find_element_by_id('com.gl365.android.merchant:id/go_to').click()
        #time.sleep(2)
       #
        driver.find_element_by_xpath('//android.widget.EditText[@index="0"]').clear()
        driver.find_element_by_xpath('//android.widget.EditText[@index="0"]').send_keys('671000165')
        print("手机号")
        driver.find_element_by_xpath('//android.widget.EditText[@text="请输入您的密码"]').send_keys('a12345678')
        print("密码")
        driver.find_element_by_xpath('//android.view.View[@text="登 录" and @index="0"]').click()
        print("登录成功")
        time.sleep(5)
