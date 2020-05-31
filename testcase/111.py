from ddt import ddt,data,unpack
#sys.path.append('./test_case')
import unittest
#from public import HttpService
from public import base
import requests
from util import handle_ini
# doc1 = 'loginByEmail'
# login = {'email': 'lidetao@163.com', 'password': 'Aa111111', 'userType': '1', 'clt': 'h5Wealth'}
#
# token = base.get_token_ok(doc1,login)
# print(token)
#
#
#
# a = handle_ini.get_value1('server','host')
# print(a)

b = base.read_jsondata('login_h5Wealth')
print(b)