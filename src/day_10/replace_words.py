#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# Created by vikey on 2018/2/10

from __future__ import print_function


def main():
    word = input("Enter what you want:")

    with open("filtered_words.txt", "r") as f:
        # 逐条替换
        for filtered_word in f.readlines():
            target_word = filtered_word.strip()

            if word.find(target_word) != -1:
                word = word.replace(target_word, "*" * int(len(target_word) / 2))

        # 输出替换后的内容
        print(word)


if __name__ == "__main__":
    main()
