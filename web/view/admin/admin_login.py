#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/7 0007 11:33
# @Author  : HelloWorld
# @File    : admin_login.py


from flask import Flask, Blueprint, jsonify, request
from passlib.apps import custom_app_context as pwd_context

admin_index = Blueprint('admin_page', __name__)

from main import db
from model.admin import Admin


@admin_index.route('/admin_login/', methods=['POST', 'GET'])
def administrator_login():
    if request.method == 'POST':
        admin_name = request.json.get('admin_name', '')
        admin_password = request.json.get('admin_password', '')
        response_msg = dict()
        response_msg['msg'] = 'alf'
        print(admin_name)
        print(admin_password)
        if all((admin_name, admin_password)):
            admin_msg = Admin.query.filter(Admin.admin_name == admin_name).first()
            if admin_msg:
                if admin_msg.verify_password(admin_password):
                    response_msg['msg'] = 'als'
                            
        return jsonify(response_msg)


@admin_index.route('/register/', methods=['POST'])
def administrator_register():
    admin_name = request.form.get('admin_name', '')
    admin_password = request.form.get('admin_password', '')
    response_msg = dict()
    response_msg['msg'] = 'fault'
    if all((admin_name, admin_password)):
        db.session.add(Admin(
            admin_name=admin_name,
            admin_password=pwd_context.encrypt(admin_password),
            permissions='1',
        ))
        db.session.commit()
        response_msg['msg'] = 'register success'

    return jsonify(response_msg)




