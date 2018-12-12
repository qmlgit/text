# coding=gbk
import sys
import time
import pygame
from aip import AipSpeech
import os

""" APPID AK SK """
APP_ID = '14383354'
API_KEY = 'jEErkIfjRBQToNBlu1Du5kmB'
SECRET_KEY = 'bBZRfLST57kNZS9Ds7OOTpIQNitVTVfL'


def getvoice(word):
    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    result = client.synthesis(word, 'zh', 3, {
         "spd":4,
        "vol":7,
        "pit":8,
        "per":1
    })

    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    if not isinstance(result, dict):
        with open('audio.mp3', 'wb') as f:
            f.write(result)

            # print('text运行')







#
# while(True):
#     word =input('单词')
#     getvoice(word)
#     # sys.exit()





