#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# Created by vikey on 2018/2/9

from __future__ import print_function
from collections import Counter


def main():
    with open("article.txt", "r") as f:
        result = Counter(f.read().split())
        for item in result.items():
            print("{}: {}".format(*item))


if __name__ == '__main__':
    main()
