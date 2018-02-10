#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# Created by vikey on 2018/2/10

from __future__ import print_function


def main():
    word = input("Enter what you want:")

    with open("filtered_words.txt", "r") as f:
        # 过滤词需要去除前后空格及换行符
        filtered_words = [filtered_word.strip() for filtered_word in f.readlines()]

        if word.strip() in filtered_words:
            print("Freedom")
        else:
            print("Human Rights")


if __name__ == "__main__":
    main()
