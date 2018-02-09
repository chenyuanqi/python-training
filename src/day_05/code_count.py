#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# Created by vikey on 2018/2/9

from __future__ import print_function
import glob
import re


def count(file_path):
    """ 统计 python 文件注释行、空行

    判断空行：非多行注释，无其他字符
    判断注释行：# 或 3 个引号开头，后者为特殊情况，出现 3 个引号则更改多行注释标志状态
    """
    comment_line = 0
    blank_line = 0
    multi_comment_flag = False

    with open(file_path, "r") as f:
        for line in f.readlines():
            if line.startswith("#"):
                comment_line += 1
            elif line.strip().startswith('"""') or line.strip().startswith("'''"):
                comment_line += 1
                multi_comment_flag = not multi_comment_flag
            elif re.match("^[\\s&&[^\\n]]*$", line):
                if multi_comment_flag:
                    comment_line += 1
                else:
                    blank_line += 1
            elif multi_comment_flag:
                comment_line += 1

    return comment_line, blank_line


def main():
    py_files = glob.glob("../day_03/*.py")
    for py_file in py_files:
        print("file: {}, comment: {}, blank: {}".format(py_file, *count(py_file)))


if __name__ == '__main__':
    main()
