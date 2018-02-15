#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# Created by vikey on 2018/2/15

from aip import AipSpeech

APP_ID = "你的 App ID"
API_KEY = "你的 Api Key"
SECRET_KEY = "你的 Secret Key"


class BaiduAip(object):
    """ 百度语音识别

        参考链接：https://cloud.baidu.com/doc/SPEECH/ASR-Online-Python-SDK.html
    """

    def __init__(self):
        self.client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

    def get_text_from_local(self, file_path, audio_format="wav"):
        try:
            with open(file_path, "rb") as f:
                result = self.client.asr(f.read(), audio_format, 16000, {
                    "lan": "zh",
                })
        except KeyError:
            print("please make sure your key right.")
        else:
            if result["err_no"] == 0:
                return result["result"][0]
            else:
                print(result["err_msg"])
