# _*_coding:utf-8 _*_
from flask import Flask, stream_with_context
from flask import Response
# from .test import getvoice


app = Flask(__name__)

@app.route('/audio')
def stream_mp3():
    def generate():
        path = 'audio.mp3'
        with open(path, 'rb') as fmp3:
            data = fmp3.read(2048)
            while data:
                yield data
                data = fmp3.read(2048)
    return Response(stream_with_context(generate()), mimetype="audio/mp3")

# if __name__ == '__main__':
#     # app.run(debug=True)
#     getvoice('hahhaha')
#     # so the other machine can visit the website by ip
#     app.run(host='0.0.0.0')
