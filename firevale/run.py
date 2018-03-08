#encoding:utf-8
import demo
import unittest

mysuite = unittest.TestSuite()

mysuite.addTest(demo.MyTestCase('testLogInHeiShi'))
#verbosity 控制log输出级别
myrunner = unittest.TextTestRunner(verbosity=2)
myrunner.run(mysuite)