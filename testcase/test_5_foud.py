from ddt import ddt,data,unpack
#sys.path.append('./test_case')
import unittest
#from public import HttpService
from public import base
import requests
from log.log import UserLog
import json
testcasefile = 'test_data.xlsx'
foud = base.get_sheet_data(testcasefile,'foud')

@ddt
class Test_Product(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.log = UserLog()
        cls.logger = cls.log.get_log()
    '''产品列表页'''
    def setUp(self) :
        self.url1 = 'https://api.haitoutech.com/haitou-order/moneyFund/generateBuyOrder'
        self.logger.info('aaaadfdsafasdfsdaf')

        # self.url2 = 'https://api.haitoutech.com/haitou-order/assetsStatistic/queryAssetsStatisticsForAll'
        # self.url3 = 'https://api.haitoutech.com/haitou-order/moneyFund/queryUserSetting'
        # self.url4 = 'https://api.haitoutech.com/haitou-order/moneyFund/queryUserAccount'
        # self.url5 = 'https://api.haitoutech.com/haitou-order/moneyFund/queryOrderList'
        # self.url6 = 'https://api.haitoutech.com/haitou-order/moneyFund/queryAccountEarningsList'
        # self.url7 = 'https://api.haitoutech.com/haitou-user/userInfo/queryUserInfoForWealth'

    @data(*foud)
    @unpack
    def test1(self,case_des,host,doc,type,code,result,orderAmount,clt,doc1,login):
        # print('测试开始！')
        # host1 = 'https://api.haitoutech.com/haitou-user/user/'
        # doc1 = 'loginByEmail'
        # url1 = ''.join([host1, doc1])
        # data1 = {'email': 'lidetao@163.com', 'password': 'Aa111111', 'userType': '1', 'clt': 'h5Wealth'}
        # r1 = requests.post(url1, data=data1,verify=False)
        # token = r1.json()["data"]
        # print(token)
        # par = {'clt':'h5Wealth','buyAmount':'100','certificationUrl':'/0fbe3e48ac1a41648db1ac726d078d78.png','token':token}
        # resp = requests.post(self.url1,data=par,verify=False)
        # print(resp)
        # dd = resp.json()['code']
        # print(dd)
        # self.assertEqual(dd,'0000',msg= '返回值错误')
        # print('测试完成！')
        print('测试开始！')

        token = base.get_token_ok(doc1,login)
        print(token)
        par = {'clt': clt,'orderAmount': orderAmount,'token':token,'certificationUrl':base.upload_file(token)}
        print(par)
        resp = requests.post(self.url1,data=par,verify=False).json()
        print(resp)
        dd = resp[code]
        print(dd)
        self.assertEqual(dd,result,msg= '返回值错误')
        print('测试完成！')
    @classmethod
    def tearDownClass(cls):
        cls.log.Close_handle()
    def tearDown(self):
        pass
if __name__ =='__main__':
    unittest.main()