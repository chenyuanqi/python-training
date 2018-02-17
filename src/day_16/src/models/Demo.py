#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# Created by vikey on 2018/2/17

from __future__ import print_function
from __future__ import unicode_literals
from flask import flash


class Demo(object):
    @classmethod
    def say_hello(cls):
        print("Hello")

    def show_text(self, text):
        if text:
            flash(text)
        else:
            flash("no text.")
