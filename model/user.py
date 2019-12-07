#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/7 0007 11:22
# @Author  : HelloWorld
# @File    : user.py

from main import db


class User(db.Model):
    __table_name__ = 'user'

    user_id = db.Column(db.INT, primary_key=True)
    user_uuid = db.Column(db.INT)
    user_name = db.Column(db.String(255))
    user_password = db.Column(db.String(255))
    level = db.Column(db.String(255))
    personality_signature = db.Column(db.String(255))
    number_followers = db.Column(db.INT)
    number_fans = db.Column(db.INT)
    uploads = db.Column(db.INT)

    def __init__(self, **kwargs):
        user_uuid = kwargs['user_uuid']
        user_name = kwargs['user_name']
        user_password = kwargs['user_password']
        level = kwargs['level']
        personality_signature = kwargs['personality_signature']
        number_followers = kwargs['number_followers']
        number_fans = kwargs['number_fans']
        uploads = kwargs['uploads']

