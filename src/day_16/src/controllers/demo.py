#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# Created by vikey on 2018/2/17

from __future__ import print_function
from __future__ import unicode_literals
from src import app
from src.models.Demo import Demo
from flask import render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class CreateForm(FlaskForm):
    text = StringField('name', validators=[DataRequired()])


@app.route('/')
def home():
    return render_template('demo/index.html')


@app.route('/demo', methods=['GET', 'POST'])
def demo():
    form = CreateForm(request.form)
    if request.method == 'POST' and form.validate():
        demo_instance = Demo()
        demo_instance.show_text(form.text.data)

        return render_template('demo/index.html')

    return render_template('demo/demo.html', form=form)
