#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
# Created by vikey on 2018/02/13

from __future__ import unicode_literals
from __future__ import print_function
import xlwt
import json


def main():
    """ write excel

    参考链接：
    http://www.python-excel.org/
    http://xlwt.readthedocs.io/en/latest/
    """
    work_book = xlwt.Workbook()
    student_sheet = work_book.add_sheet("student")

    with open("student.txt", "r") as f:
        file_content = f.read()
        file_dict = json.loads(file_content)
        file_line = 0

        for key, value in file_dict.items():
            # sheet.write(row_number, col_number, sheet_content, sheet_style)
            student_sheet.write(file_line, 0, key)
            for file_key, file_value in enumerate(value):
                student_sheet.write(file_line, file_key + 1, file_value)
            # 行号自增
            file_line = file_line + 1

        work_book.save("student.xls")


if __name__ == "__main__":
    main()
