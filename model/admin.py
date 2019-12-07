#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/7 0007 11:28
# @Author  : HelloWorld
# @File    : admin.py

from main import db
from passlib.apps import custom_app_context as pwd_context


class Admin(db.Model):
    __table_name__ = 'admin'
    admin_di = db.Column(db.INT, primary_key=True)
    admin_name = db.Column(db.String(255))
    admin_password = db.Column(db.String(255))
    permissions = db.Column(db.String(255))

    def __init__(self, **kwargs):
        self.admin_name = kwargs['admin_name']
        self.admin_password = kwargs['admin_password']
        self.permissions = kwargs['permissions']

    def hash_password(self, admin_password):
        self.admin_password = pwd_context.encrypt(admin_password)

    def verify_password(self, admin_password):
        return pwd_context.verify(admin_password, self.admin_password)
