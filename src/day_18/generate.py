#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# Created by vikey on 2018/3/1

from __future__ import print_function
from __future__ import unicode_literals


def generate_number():
    for index in range(1, 10):
        yield index


def main():
    data = generate_number()
    for index in data:
        print(index)


if __name__ == "__main__":
    main()
