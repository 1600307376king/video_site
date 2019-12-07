#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/7 0007 11:33
# @Author  : HelloWorld
# @File    : admin_login.py


from flask import Flask, Blueprint, jsonify, request

admin_index = Blueprint('admin_page', __name__)

from main import db
from model.admin import Admin


@admin_index.route('/admin_login/', methods=['POST', 'GET'])
def administrator_login():
    if request.method == 'POST':
        user_name = request.form.get('user_name', '')
        admin_password = request.form.get('admin_password', '')
        response_msg = dict()
        response_msg['msg'] = 'alf'
        if all((user_name, admin_password)):
            admin_msg = Admin.query.filter(Admin.user_name == user_name).first()
            if admin_msg:
                if admin_msg.admin_password == admin_password:
                    response_msg['msg'] = 'als'

        return jsonify(response_msg)




