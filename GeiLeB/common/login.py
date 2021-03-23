from appium import webdriver
import unittest,time



def get_driver():

    desired_capabilities = {
        'platformName': 'Android',
        "platformVersion": '8',
        "deviceName": 'android',
        "appPackage": "com.gl365.android.merchant",
        "appActivity": ".MainActivity",
        #uiautomator2 是一个可以使用Python对Android设备进行UI自动化的库
        'automationName': 'uiautomator2',
        "noReset": 'True'  # ,true app不初始化
    }
    #
    driver = webdriver.Remote('http://192.168.0.160:4723/wd/hub', desired_capabilities)

    # 隐式等待
    driver.implicitly_wait(10)
    return driver


