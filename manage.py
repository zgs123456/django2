# -*- coding:utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import redis
app = Flask(__name__)

class Config(object):
    """工程配置信息"""
    DEBUG = True
    #mysql
    SQLALCHEMY_DATABASE_URI='mysql://root:mysql@127.0.0.1:3306/ihome'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #redis
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

app.config.from_object(Config)
db = SQLAlchemy(app)
redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)

@app.route('/index')
def index():
    return 'index'

if __name__ == '__main__':
    app.run()