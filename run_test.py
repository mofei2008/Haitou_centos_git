#coding=utf-8
#!usr/bin/python
#from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import unittest
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import time,os,sys
sys.path.append('./testcase')
#sys.path.append('./')
# from HTMLTestRunnerCN import HTMLTestRunner

from public import base,HTMLTestRunnerCN

#在测试报告目录下找到最新的报告文件,打印且返回最新报告的名称
def report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport+"/"+fn))
    filename = os.path.join(testreport,lists[-1])
    print("报告已生成：%s" % filename)
    return filename

if __name__ =="__main__":
    #构建测试集
    test_dir = './testcase'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    filename = './report/' + now + '_result.html'
    fp = open(filename,"wb")
    runner = HTMLTestRunnerCN.HTMLTestRunner(stream=fp,
                            title="海投系统接口测试",
                            description="以下是接口测试结果",
                            verbosity=2)
    runner.run(discover)
    fp.close()
    test_report = '/opt/Haitou_centos_git/report'
    rep = report(test_report)
#    rep = base.report(test_report)
    #print(rep)
    #发送邮件

    base.send_mail(rep)
    base.send_mail(rep)
   # print("Email has send out")