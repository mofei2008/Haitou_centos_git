from ddt import ddt,data,unpack
#sys.path.append('./test_case')
import unittest
#from public import HttpService
from public import base
import requests

testcasefile = 'test_data.xlsx'
order2 = base.get_sheet_data(testcasefile,'order2')

@ddt
class Test_OrderT(unittest.TestCase):
    '''订单提交页'''
    def setUp(self) :
         self.url1 = 'https://api.haitoutech.com/haitou-order/order/confirmOrderInfo'
         #self.url2 = 'https://api.haitoutech.com//haitou-order/rechargeOrder/generateRechargeOrder'
        # self.url3 = 'https://api.haitoutech.com/haitou-order/moneyFund/queryUserSetting'
        # self.url4 = 'https://api.haitoutech.com/haitou-order/moneyFund/queryUserAccount'
        # self.url5 = 'https://api.haitoutech.com/haitou-order/moneyFund/queryOrderList'
        # self.url6 = 'https://api.haitoutech.com/haitou-order/moneyFund/queryAccountEarningsList'
        # self.url7 = 'https://api.haitoutech.com/haitou-user/userInfo/queryUserInfoForWealth'

    @data(*order2)
    @unpack
    def test2(self,case_des,host,doc,doc2,type,code,result,returnType,productType,orderAmount,clt,doc1,login):
        print('测试开始！')
        url = ''.join([host, doc])
        url3 =  ''.join([host, doc2])
        token = base.get_token_ok(doc1, login)
        par = {'clt':clt,'returnType':returnType,'productType':productType,'token':token}
        # par = {'clt': 'h5Wealth', 'returnType': '151', 'productType': '340', 'token': '5c3fd464-d220-439f-a8c7-9ad624f30394'}
        resp = base.get_ProId(data=par)
        # print(resp)
        # dd = resp['data']
        # # print(dd)
        dd = resp['data'][3]['id']
        print(dd)
        par2 = {'clt':clt,'productId':dd,'orderAmount':orderAmount,'balanceCurrencyType':'USD','token':token}
        resp2 = base.method(url,method=type,data=par2)
        print(resp2)
        # print(resp1)
        orderNo = resp2['data']['orderNo']
        print(orderNo)
        par3 = {'clt':clt,'productId':dd,'orderNo':orderNo,'token':token}
        print(par3)
        # resp3 = base.method(url3,method=type,data=par3)
        # print(resp3)
        self.assertEqual(resp[code],result,msg= '返回值错误')
        print('测试完成！')
    # @data(*product)
    # @unpack
    # def test3(self,case_des,host,doc,type,code,result,returnType,productType,clt,doc1,login):
    #     print('测试开始！')
    #     url = ''.join([host, doc])
    #     token = base.get_token_ok(doc1, login)
    #     par = {'clt':clt,'returnType':returnType,'productType':productType,'token':token}
    #     resp = base.method(url,method=type,data=par)
    #     # print(resp)
    #     dd = resp['data']
    #     # print(dd)
    #     aa = dd[2]['id']
    #     print(aa)
    #     par1 = {'clt':clt,'productId':aa,'orderAmount':'10000','token':token}
    #     resp1 = base.method(self.url1,method=type,data=par1)
    #     print(resp1)
    #     par2 = {'clt':clt,'productId':aa,'orderAmount':'10000','balanceCurrencyType':'CNY','token':token}
    #     resp2 = base.method(self.url2,method=type,data=par2)
    #     print(resp2)
    #     # infolist = []
    #     # for row in range(1,self.rows):
    #     #     info = self.sheet.row_values(row)
    #     #     infolist.append(info)
    #
    #     #self.assertTrue(resp[code] == result)
    #     self.assertEqual(resp[code],result,msg= '返回值错误')
    #     print('测试完成！')
    def tearDown(self):
        pass
if __name__ =='__main__':
    unittest.main()