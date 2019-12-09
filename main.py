from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_cors import CORS, cross_origin
import os
from datetime import timedelta


class Main(Flask):
    def __init__(self, name, template_folder=None, static_folder=None):
        super(Main, self).__init__(name, template_folder=template_folder, static_folder=static_folder)
        self.config['JSON_AS_ASCII'] = False
        self.config.from_pyfile('config/development_setting.py')
        self.config['SECRET_KEY'] = os.urandom(24)  # 设置为24位的字符,每次运行服务器都是不同的，所以服务器启动一次上次的session就清除
        self.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)  # 设置session的保存时间
        self.config.setdefault('SQLALCHEMY_POOL_SIZE', 100)
        self.config.setdefault('SQLALCHEMY_MAX_OVERFLOW', 20)
        db.init_app(self)


db = SQLAlchemy()
app = Main(__name__, template_folder=os.getcwd() + '/web/templates/',
           static_folder=os.getcwd() + "/web/static/")
# manager = Manager(app)
CORS(app, supports_credentials=True)
from web.view.video.video import video_index
from web.view.admin.admin_login import admin_index


app.register_blueprint(video_index, url_prefix='/')
app.register_blueprint(admin_index, prefix_url='/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
