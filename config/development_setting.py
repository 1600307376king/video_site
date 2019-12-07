#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/7 0007 10:03
# @Author  : HelloWorld
# @File    : development_setting.py


import os

SERVER_PORT = '8099'
IP = '127.0.0.1'
URL = 'http://' + IP + ':' + SERVER_PORT
STATIC_FILE_PATH = os.getcwd() + '/web/static'

# 分页每页最大数
PER_PAGE_MAX_NUM = 5

DEBUG = False
SQLALCHEMY_ECHO = False

SQLALCHEMY_ENCODING = 'utf-8'

# 该配置为True,则每次请求结束都会自动commit数据库的变动
SQLALCHEMY_TRACK_MODIFICATIONS = False

# session必须要设置key
SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

# mysql数据库连接信息
DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD = ''
HOST = 'localhost'
PORT = '3306'
DATABASE = 'video'
# 这个连接字符串变量名是固定的具体 参考 flask_sqlalchemy 文档 sqlalchemy会自动找到flask配置中的 这个变量
SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT,
                                                                       DATABASE)
