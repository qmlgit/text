'''谷歌翻译英译汉第一版，汉议英无效'''

import requests
import json
import execjs #sudo pip3 install pyExecJS 导入该模块即可

#谷歌翻译ＡＰＩ口的破解，调用大神的tk算法
class Py4Js():
    def __init__(self):
        self.ctx = execjs.compile("""
        function TL(a) {
        var k = "";
        var b = 406644;
        var b1 = 3293161072;
        
        var jd = ".";
        var $b = "+-a^+6";
        var Zb = "+-3^+b+-f";
    
        for (var e = [], f = 0, g = 0; g < a.length; g++) {
            var m = a.charCodeAt(g);
            128 > m ? e[f++] = m : (2048 > m ? e[f++] = m >> 6 | 192 : (55296 == (m & 64512) && g + 1 < a.length && 56320 == (a.charCodeAt(g + 1) & 64512) ? (m = 65536 + ((m & 1023) << 10) + (a.charCodeAt(++g) & 1023),
            e[f++] = m >> 18 | 240,
            e[f++] = m >> 12 & 63 | 128) : e[f++] = m >> 12 | 224,
            e[f++] = m >> 6 & 63 | 128),
            e[f++] = m & 63 | 128)
        }
        a = b;
        for (f = 0; f < e.length; f++) a += e[f],
        a = RL(a, $b);
        a = RL(a, Zb);
        a ^= b1 || 0;
        0 > a && (a = (a & 2147483647) + 2147483648);
        a %= 1E6;
        return a.toString() + jd + (a ^ b)
    };
    
    function RL(a, b) {
        var t = "a";
        var Yb = "+";
        for (var c = 0; c < b.length - 2; c += 3) {
            var d = b.charAt(c + 2),
            d = d >= t ? d.charCodeAt(0) - 87 : Number(d),
            d = b.charAt(c + 1) == Yb ? a >>> d: a << d;
            a = b.charAt(c) == Yb ? a + d & 4294967295 : a ^ d
        }
        return a
    }
    """)   
    def getTk(self,text):
        return self.ctx.call("TL",text)
 
class Gg_fanyi:
    def __init__(self, word,tk):
        self.url = 'https://translate.google.cn/translate_a/single?client=t&sl=en&tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&otf=2&ssel=0&tsel=0&tk=%s&q='%tk+word
        self.url1='https://translate.google.cn/translate_tts?ie=UTF-8&q=%s&tl=en&total=1&idx=0&textlen=3&tk=%s&client=t&prev=input'%(word,tk)
        self.headers = {'User-Agent': 'Mozilla/4.0(Windows; U;MSIE 6.0; Windows NT 6.1; SV1; .NET CLR 2.0.50727)'
}

    def request_get(self):
        self.res = requests.get(self.url, headers=self.headers)
        self.response = self.res.text
        self.html = json.loads(self.response)
        return self.html

    def get_vedio(self):
        self.res = requests.get(self.url1, headers=self.headers)
        self.response=self.res.content


        framerate = 8000
        # time = 10

        # 产生10秒44.1kHz的100Hz - 1kHz的频率扫描波
        # t = np.arange(0, time, 1.0 / framerate)
        # self.response = signal.chirp(self.response, 100, 10, 1000, method='linear') * 10000
        # self.response = self.response.astype(np.short)

        # 打开WAV文档
        with open(r"zm.mp3", "wb") as f:

        # 配置声道数、量化位数和取样频率
        # f.setnchannels(1)
        # f.setsampwidth(2)
        # f.setframerate(framerate)
        # 将wav_data转换为二进制数据写入文件
            f.write(self.response)

            f.close()

    def request_result(self):
        self.html=self.request_get()
        self.result = self.html[0][0][0]
        return self.result

# if __name__ == '__main__':
def getfanyi(content):
    # content=input("请输入你要翻译的内容：")
    TK=Py4Js()
    tk=TK.getTk(content)
    s = Gg_fanyi(content,tk)
    result = s.request_result()
    return result
    # vedio=s.get_vedio()
    # print('翻译结果:',result)

