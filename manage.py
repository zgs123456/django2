# -*- coding:utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import redis
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
app = Flask(__name__)


class Config(object):
    """工程配置信息"""
    DEBUG = True
    SECRET_KEY = "EjpNVSNQTyGi1VvWECj9TvC/+kq3oujee2kTfQUs8yCM6xX9Yjq52v54g+HVoknA"
    # mysql
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1:3306/ihome'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # redis
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379
    # flask_session配置信息
    SESSION_TYPE='redis'
    SESSION_USE_SINGER=True
    SESSION_REDIS=redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    PERMANENT_SESSION_LIFETIME = 86400
app.config.from_object(Config)
db = SQLAlchemy(app)
redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
app.config.from_object(Config)
csrf=CSRFProtect(app)
Session(app)

@app.route('/index')
def index():
    return 'index'


if __name__ == '__main__':
    app.run()
