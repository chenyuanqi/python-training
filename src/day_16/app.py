#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# Created by vikey on 2018/2/17

from __future__ import print_function
from __future__ import unicode_literals
import os
from src import app


def main():
    port = os.environ.get("PORT", 8080)
    app.run("0.0.0.0", port=port)


if __name__ == "__main__":
    main()
