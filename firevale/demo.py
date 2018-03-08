#encoding:utf-8
import unittest
from appium import webdriver
import time
import os
from OCR import *

class MyTestCase(unittest.TestCase):
    ocr = Ocr()
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'com.firevale.coclua.device'
        desired_caps['appActivity'] = 'com.firevale.coclua.Main'

        # 中文支持
        desired_caps['unicodeKeyboard'] = 'True'
        desired_caps['resetKeyboard'] = 'True'

        # api接口
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def testLogInHeiShi(self):
        time.sleep(20)
        self.driver.tap([('951', '744')], 3)
        print('点击进入游戏')
        time.sleep(10)
        self.driver.tap([('1709', '49')], 3)
        print('点击关闭公告')
        time.sleep(5)
        self.driver.tap([('1826', '316')], 3)
        print('点击进入奇遇')
        time.sleep(5)
        self.driver.tap([('816', '901')], 3)
        print('点击进入黑市')
        for n in range(1, 33):
            print('第%s页'%n)
            time.sleep(5)
            self.driver.tap([('354', '685')], 3)
            MyTestCase.ocr.run()
            time.sleep(5)
            self.driver.tap([('1706', '286')], 3)
            MyTestCase.ocr.run()
            time.sleep(5)
            self.driver.tap([('763', '685')], 3)
            MyTestCase.ocr.run()
            time.sleep(5)
            self.driver.tap([('1706', '286')], 3)
            MyTestCase.ocr.run()
            time.sleep(5)
            self.driver.tap([('1167', '685')], 3)
            MyTestCase.ocr.run()
            time.sleep(5)
            self.driver.tap([('1706', '286')], 3)
            MyTestCase.ocr.run()
            time.sleep(5)
            self.driver.tap([('1571', '685')], 3)
            MyTestCase.ocr.run()
            time.sleep(5)
            self.driver.tap([('1706', '286')], 3)
            MyTestCase.ocr.run()
            time.sleep(5)
            self.driver.swipe('1718', '439', '910', '468', 3)
            print('进入下一页')
            time.sleep(5)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
