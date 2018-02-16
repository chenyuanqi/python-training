#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# Created by vikey on 2018/2/16

from __future__ import print_function
from __future__ import unicode_literals
from flask import Flask

# pip3 install Flask
app = Flask(__name__)


@app.route("/")
def home():
    return "Home page."


def main():
    # 开启调试模式
    app.debug = True
    # 指定 host 和 port，host=0.0.0.0 代表支持公开 ip
    # port 默认 5000
    app.run(host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
