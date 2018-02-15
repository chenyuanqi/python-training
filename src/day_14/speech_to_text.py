#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# Created by vikey on 2018/2/14

from __future__ import print_function
from __future__ import unicode_literals
# brew install portaudio
# pip3 install pyaudio
from BaiduAip import BaiduAip
from datetime import datetime
import wave
import pyaudio
import webbrowser
import os


def record_wave():
    audio_format = pyaudio.paInt16
    audio_channel = 1
    audio_rate = 16000
    audio_chunk = 1024
    audio_record_second = 5

    pyaudio_instance = pyaudio.PyAudio()
    stream = pyaudio_instance.open(format=audio_format,
                                   channels=audio_channel,
                                   rate=audio_rate,
                                   input=True,
                                   frames_per_buffer=audio_chunk)

    print("* recording...")

    save_buffer = []
    for i in range(0, int(audio_rate / audio_chunk * audio_record_second)):
        audio_data = stream.read(audio_chunk)
        save_buffer.append(audio_data)

    print("* done.")

    # 停止录音
    stream.stop_stream()
    stream.close()
    pyaudio_instance.terminate()

    # 录音文件路径构建
    file_name = datetime.now().strftime("%Y-%m-%d_%H_%M_%S") + ".wav"
    file_path = "./" + file_name

    # 保存文件
    wf = wave.open(file_path, 'wb')
    wf.setnchannels(audio_channel)
    wf.setsampwidth(pyaudio_instance.get_sample_size(audio_format))
    wf.setframerate(audio_rate)
    wf.writeframes(b"".join(save_buffer))
    wf.close()

    return file_path


def open_browser_by_text(text):
    if text is None:
        return

    if text.find("谷歌") != -1 or text.find("google") != -1:
        url = "http://www.google.com"
    elif text.find("必应") != -1 or text.find("bing") != -1:
        url = "http://cn.bing.com"
    else:
        url = "http://www.baidu.com"

    webbrowser.open_new_tab(url)


def main():
    # 保存录音到当前文件夹
    file_path = record_wave()
    # 百度语音识别
    aip_instance = BaiduAip()
    record_text = aip_instance.get_text_from_local(file_path)
    # 删除录音文件
    os.remove(file_path)

    # 根据录音文本，使用默认浏览器打开相应链接
    open_browser_by_text(record_text)


if __name__ == "__main__":
    main()
