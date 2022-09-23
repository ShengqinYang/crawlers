# -*- coding: utf-8 -*-
'''
@author:
@date: 20210706
@purpose:
'''

import pymysql
from config import Config


class MySQLConnection(object):
    '''
    mysql 连接：
    usage:
    with MySQLConnection() as conn:
        cursor = conn.cursor()
    '''
    def __init__(self, db_host='mysql_conf', **kwargs):
                #  user=None, password="",
                #  database=None, port=0, unix_socket=None,
                #  charset=None, sql_mode=None,
                #  read_default_file=None, conv=None, use_unicode=None,
                #  client_flag=0, init_command=None,
                #  connect_timeout=None, ssl=None, read_default_group=None,
                #  compress=None, named_pipe=None, no_delay=None,
                #  autocommit=False, passwd=None, local_infile=False,
                #  max_allowed_packet=16*1024*1024, defer_connect=False,
                #  auth_plugin_map={}, read_timeout=None, write_timeout=None
        db_host = str(db_host)
        if db_host == "158": # 兼容其他调用方式
            db_host = 'mysql_conf_158'
        elif db_host == "85":
            db_host = 'mysql_85'
        elif db_host == "150":
            db_host = 'mysql_conf'
        elif db_host == "60":
            db_host = 'mysql_conf_DSP'
        else:
            pass
        if db_host in {'mysql_conf', 'mysql_conf_zilongreport', 
                         'mysql_conf_DSP', 'mysql_85', 'mysql_conf_158'}:
            self.__host = getattr(Config, db_host).get('host', '')
            self.__port = getattr(Config, db_host).get('port', '')
            self.__user = getattr(Config, db_host).get('user', '')
            self.__password = getattr(Config, db_host).get('password', '')
            self.__charset = getattr(Config, db_host).get('charset', '')
            # 去掉从参数中可能带过来的参数
            for each in {'host', 'port', 'user', 'password', 'charset'}:
                if each in kwargs.keys():
                    kwargs.pop(each)
            self.conn = pymysql.connect(host=self.__host, port=self.__port,
                                        user=self.__user, password=self.__password,
                                        charset=self.__charset, **kwargs)
            self.cur = self.conn.cursor
        else:
            raise Exception('There is no match conf: {} '.format(db_host))

    @property
    def cursor(self):
        return self.cur

    def commit(self):
        return self.conn.commit()

    def __enter__(self):
        return self.conn

    def __exit__(self, exc_type, exc_value, traceback):
        if self.conn:
            self.conn.commit()
            self.conn.close()

MysqlDataSource = MySQLConnection

if __name__ == "__main__":
    print(MySQLConnection(123))