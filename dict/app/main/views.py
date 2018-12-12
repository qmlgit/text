from flask import render_template, request, session, redirect,json
#导入蓝图程序 用于构建路由
from . import main
#导入db用于操作数据库
from .. import db
#导入实体类
from .. models import *

@main.route('/signup',methods=['POST','GET'])
def signup():
    if request.method == 'GET':
        return render_template('index1.html',params=locals())
    else:
        name = request.form.get('uname')
        username = request.form.get('sname')
        print(username)
        if username:
            uemail = request.form.get('semail')
            upwd1 = request.form.get('spwd1')
            upwd2 = request.form.get('spwd2')
            u = Users.query.filter_by(username=username).first()
            if u:
                h = 1
                return render_template('index1.html',params=locals())
            elif upwd1 == upwd2:
                j = 1
                user = Users(username,upwd1)
                db.session.add(user)
                db.session.commit()
                return render_template('index1.html',params=locals())
            else:
                i = 1
                return render_template('index1.html',params=locals())
        if name:
            password = request.form.get('upwd')
            u = Users.query.filter_by(username=name,password=password).first()
            if u:
                return redirect('/query')
            else:
                k = 1
                return render_template('index1.html',params=locals())

@main.route('/query')
def querya():
    return render_template('index11.html')
@main.route('/find')
def findword():
    word = request.args.get('word')
    result = Words.query.filter_by(word = word).first()
    if result:
        return json.dumps(result.to_dict())
    else:
        return redirect('find1?word='+word)


