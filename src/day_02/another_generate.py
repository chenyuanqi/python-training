#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# Created by vikey on 2018/2/8

import uuid


def main():
    with open("another_keys.txt", "w") as f:
        for index in range(200):
            f.write(str(uuid.uuid1()) + "\n")


if __name__ == '__main__':
    main()
