import requests
import unittest
import json
import time,os,sys
from ddt import ddt,data,unpack
sys.path.append('./test_case')
#from public import HttpService
from public import base
from log.log import UserLog


testcasefile = 'test_data.xlsx'
login = base.get_sheet_data(testcasefile,'login')
#TestData = base.get_data(testcasefile,'TestData')
# print(login)
@ddt
class Test_Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.log = UserLog()
        cls.logger = cls.log.get_log()
    '''登录功能'''
    def setUp(self) :
        print('测试开始！')
        self.logger.debug('日志打印开始')
    @data(*login)
    @unpack
    def test1(self,case_des,host,doc,code,result,type1,par):
        url = ''.join([host, doc])
        par = eval(par)
        print(par)
        print(type(par))
        # print(data)
        r = base.method(url,type1,data=par)
        self.assertTrue(r[code] == result)
        print(r)
        print('测试完成！')
    @classmethod
    def tearDownClass(cls):
        cls.log.Close_handle()
    def tearDown(self):
        pass