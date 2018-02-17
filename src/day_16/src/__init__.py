#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# Created by vikey on 2018/2/17

from __future__ import print_function
from __future__ import unicode_literals
from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension


app = Flask("src")
app.config["SECRET_KEY"] = "random"
app.debug = True

toolbar = DebugToolbarExtension(app)

from src.controllers import *
