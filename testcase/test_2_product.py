from ddt import ddt,data,unpack
#sys.path.append('./test_case')
import unittest
#from public import HttpService
from public import base
import requests

testcasefile = 'test_data.xlsx'
product = base.get_sheet_data(testcasefile,'product')

@ddt
class Test_Product(unittest.TestCase):
    '''产品列表页'''
    def setUp(self) :
         self.url1 = 'https://api.haitoutech.com/haitou-order/assetsStatistic/queryAssetsStatisticsForRegularEarnings'
        # self.url2 = 'https://api.haitoutech.com/haitou-order/assetsStatistic/queryAssetsStatisticsForAll'
        # self.url3 = 'https://api.haitoutech.com/haitou-order/moneyFund/queryUserSetting'
        # self.url4 = 'https://api.haitoutech.com/haitou-order/moneyFund/queryUserAccount'
        # self.url5 = 'https://api.haitoutech.com/haitou-order/moneyFund/queryOrderList'
        # self.url6 = 'https://api.haitoutech.com/haitou-order/moneyFund/queryAccountEarningsList'
        # self.url7 = 'https://api.haitoutech.com/haitou-user/userInfo/queryUserInfoForWealth'

    @data(*product)
    @unpack
    def test1(self,case_des,host,doc,type,code,result,returnType,productType,clt,doc1,login):
        print('测试开始！')
        # a = 'loginByEmail'
        # b = {'email': 'lidetao@163.com', 'password': 'Aa111111', 'userType': '1', 'clt': 'h5Wealth'}
        url = ''.join([host, doc])
        par = {'clt':clt,'returnType':returnType,'productType':productType,'token':base.get_token_ok(doc1,login)}
        resp = base.method(url,method=type,data=par)
        # print(resp)
        dd = resp['data']
        print(dd)
        aa = dd[1]['id']
        # infolist = []
        # for row in range(1,self.rows):
        #     info = self.sheet.row_values(row)
        #     infolist.append(info)
        print(aa)
        #self.assertTrue(resp[code] == result)
        self.assertEqual(resp[code],result,msg= '返回值错误')
        print('测试完成！')

    def tearDown(self):
        pass
