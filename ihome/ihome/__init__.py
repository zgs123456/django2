# coding=utf8
import logging
from logging.handlers import RotatingFileHandler

import redis
from flask import Flask
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

from config import Config
from config import config
from ihome.utils.commons import RegexConverter

# 数据库
db = SQLAlchemy()
redis_store = None
def set_logging(log_level):

    # 设置日志的记录等级
    logging.basicConfig(level=log_level)  # 调试debug级
    # 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
    file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024*1024*100, backupCount=10)
    # 创建日志记录的格式                 日志等级    输入日志信息的文件名 行数    日志信息
    formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
    # 为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象（flask app使用的）添加日志记录器
    logging.getLogger().addHandler(file_log_handler)

# 开启保护

csrf = CSRFProtect()

# 创建app工厂
def create_app(config_name):
    app = Flask(__name__)
    # 配置
    config_cls=config[config_name]
    app.config.from_object(config_cls)
    # 初始化
    db.init_app(app)
    # 日志等级
    set_logging(config_cls.LOG_LEVEL)
    # 设置redis
    global redis_store
    redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
    # 开启session
    Session(app)
    # 开启csrf保护
    CSRFProtect(app)
    # 添加自定义路由转换器
    app.url_map.converters['re'] = RegexConverter

    # 注册蓝图，在使用的时候再引入
    from . import api_1_0
    app.register_blueprint(api_1_0.api, url_prefix='/api/v1.0')
    # 注册html静态文件的蓝图
    from ihome.web_html import html
    app.register_blueprint(html)

    return app
