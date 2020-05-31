#coding=utf-8
import logging
import os
import datetime

class UserLog(object):
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        #控制台日志
        # consle = logging.StreamHandler()
        # logger.addHandler(consle)
        # logger.debug('2112')
        # consle.close()
        # logger.removeHandler(consle)
        #文件名字
        base_dir = os.path.dirname(os.path.abspath(__file__))
        print(os.path.dirname(os.path.abspath(__file__)))
        log_dir = os.path.join(base_dir,'logs')
        print(os.path.join(base_dir,'logs'))
        print(datetime.datetime.now().strftime('%Y-%m-%d %H_%M_%S'))
        print(datetime.datetime.now().strftime('%Y-%m-%d'))
        log_file = datetime.datetime.now().strftime('%Y-%m-%d') +'.log'
        log_name = log_dir + '/' + log_file
        print(log_name)

        #文件输出日志
        self.file_handle = logging.FileHandler(log_name,'a',encoding='utf-8')
        '''日志级别'''
        self.file_handle.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s %(filename)s %(funcName)s %(lineno)d %(levelname)s ---> %(message)s')
        self.file_handle.setFormatter(formatter)
        self.logger.addHandler(self.file_handle)
        # self.logger.debug('jjj')
        # self.file_handle.close()
        # self.logger.removeHandler(self.file_handle)
    def get_log(self):
        return self.logger

    def Close_handle(self):
        self.logger.removeHandler(self.file_handle)
        self.file_handle.close()

if __name__ == '__main__':
    user = UserLog()
    log = user.get_log()
    log.debug('aaa')
    user.Close_handle()