# coding=utf-8
from flask import Blueprint, current_app, make_response
from flask_wtf.csrf import generate_csrf

html = Blueprint('html', __name__)


@html.route('/<re(".*"):file_name>')
def get_html(file_name):
    # 提供静态文件
    if not file_name:
        file_name = 'index.html'
    if file_name != "favicon.ico":
        file_name = 'html/' + file_name
    # return current_app.send_static_file(file_name)


    csrf_token=generate_csrf()
    #将csrf_token添加带cookie中
    response=make_response(current_app.send_static_file(file_name))
    response.set_cookie("csef_token",csrf_token)
    return response
