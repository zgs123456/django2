# -*- coding:utf-8 -*-

from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from ihome import create_app,db
#创建APP 并传入配置
app = create_app('development')
manager = Manager(app)
Migrate(app, db)
manager.add_command('db', MigrateCommand)




@app.route('/index')
def index():
    return 'index'


if __name__ == '__main__':
    manager.run()
