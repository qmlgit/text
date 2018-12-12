from . import reptile
from flask import render_template, request, json
from .GuGe_FanYi import getfanyi

@reptile.route('/find1')
def fanyi():
    word = request.args.get('word')
    fanyi = getfanyi(word)
    dic = {
        'interpret':fanyi
    }
    return json.dumps(dic)

