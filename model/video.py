#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/7 0007 10:02
# @Author  : HelloWorld
# @File    : video.py

from main import db


class Video(db.Model):
    __table_name__ = 'video'
    v_id = db.Column(db.INT, primary_key=True)
    video_name = db.Column(db.String(255))
    video_url = db.Column(db.String(255))
    play_volume = db.Column(db.INT)
    video_labels = db.Column(db.String(255))
    up_id = db.Column(db.INT)
    video_category = db.Column(db.String(255))

    def __init__(self, **kwargs):
        self.v_id = kwargs['video_name']
        self.video_name = kwargs['video_name']
        self.video_url = kwargs['video_url']
        self.play_volume = kwargs['play_volume']
        self.video_labels = kwargs['video_labels']
        self.up_id = kwargs['up_id']
        self.video_category = kwargs['video_category']

