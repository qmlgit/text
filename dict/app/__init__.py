from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
    app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost:3306/flask'
    #配置数据库内容更新时自动提交
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
    #配置session所需要的密钥
    app.config['SECRET_KEY']='you guess'
    #数据库的初始化
    db.init_app(app)

    #将mian蓝图程序与app关联到一起
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .reptile import reptile as reptile_blueprint
    app.register_blueprint(reptile_blueprint)
    from .voice import voice as voice_blueprint
    app.register_blueprint(voice_blueprint)
    return app
