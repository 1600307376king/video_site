#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/7 0007 9:53
# @Author  : HelloWorld
# @File    : video.py


from flask import Flask, Blueprint, jsonify


video_index = Blueprint('video_page', __name__)

from main import db
from model.video import Video


@video_index.route('/')
def video_home():
    video_msg = Video.query.filter()
    response_msg = dict()
    response_msg['video_name'] = 'hello'
    return jsonify(response_msg)


@video_index.route('/upload/<int:uuid>', methods=['GET', 'POST'])
def upload_user_video(uuid):
    if not uuid:
        return jsonify({'msg', 'plz_login'})

    return jsonify({'msg', 'success'})



