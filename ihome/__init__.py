#coding=utf8
import redis
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from config import Config

#数据库
db=SQLAlchemy()
redis_store=None
#开启保护
csrf=CSRFProtect()

#创建app工厂
def create_app(config_name):
    app=Flask(__name__)
    # 配置
    app.config.from_object(Config)
    #初始化
    db.init_app(app)
    # 设置redis
    global redis_store
    redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
    #开启session
    Session(app)
    #开启csrf保护
    csrf.init_app(app)

    return app


