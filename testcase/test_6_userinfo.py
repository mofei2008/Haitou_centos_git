from ddt import ddt,data,unpack
#sys.path.append('./test_case')
import unittest
#from public import HttpService
from public import base
import requests
import json
testcasefile = 'test_data.xlsx'
usertype = base.get_sheet_data(testcasefile,'usertype')

@ddt
class Test_Product(unittest.TestCase):
    '''产品列表页'''
    def setUp(self) :
         self.url1 = 'https://api.haitoutech.com/haitou-user/userInfo/queryUserInfoForWealth'
        # self.url2 = 'https://api.haitoutech.com/haitou-order/assetsStatistic/queryAssetsStatisticsForAll'
        # self.url3 = 'https://api.haitoutech.com/haitou-order/moneyFund/queryUserSetting'
        # self.url4 = 'https://api.haitoutech.com/haitou-order/moneyFund/queryUserAccount'
        # self.url5 = 'https://api.haitoutech.com/haitou-order/moneyFund/queryOrderList'
        # self.url6 = 'https://api.haitoutech.com/haitou-order/moneyFund/queryAccountEarningsList'
        # self.url7 = 'https://api.haitoutech.com/haitou-user/userInfo/queryUserInfoForWealth'

    @data(*usertype)
    @unpack
    def test1(self,case_des,host,doc,type,code,result,userType,clt,doc1,login):
        print('测试开始！')
        url = ''.join([host, doc])
        par = {'clt':clt,'token':base.get_token_ok(doc1,login)}
        resp = base.method(url,method=type,data=par)
        print(resp)
        r1 = resp['data']['investorAuditStatus']
        self.assertEqual(resp[code],result,msg= '返回值错误')
        # self.assertEqual(str(r1),userType,msg='用户返回类型不对')
        userType = int(userType)
        self.assertEqual(r1,userType,msg='用户返回类型不对')
        print(userType)

        print('测试完成！')

    def tearDown(self):
        pass
if __name__ =='__main__':
    unittest.main()