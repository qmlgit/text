from . import voice
from flask import request, json, Response, redirect, stream_with_context
from .test import getvoice

@voice.route('/voice')
def voice_views():
    word = request.args.get('word')
    getvoice(word)
    # return redirect('/audio')
    def generate():
        path = 'audio.mp3'
        with open(path, 'rb') as fmp3:
            data = fmp3.read(2048)
            while data:
                yield data
                data = fmp3.read(2048)
            # print('发过去了')
    return Response(generate(), mimetype="audio/mp3")

# @voice.route('/audio')
# def stream_mp3():
#     def generate():
#         path = 'audio.mp3'
#         with open(path, 'rb') as fmp3:
#             data = fmp3.read(2048)
#             while data:
#                 yield data
#                 data = fmp3.read(2048)
#     return Response(generate(), mimetype="audio/mp3")



