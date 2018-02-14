#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# Created by vikey on 2018/2/13

from __future__ import print_function
from __future__ import unicode_literals
import xlrd
import xml.dom.minidom
import json


def main():
    """ read excel

    参考链接：
    https://github.com/python-excel/xlrd
    http://xlrd.readthedocs.io/en/latest/
    """

    # 读取 excel 文件
    workbook = xlrd.open_workbook("student.xls", formatting_info=True, encoding_override="utf-8")
    sheet = workbook.sheet_by_index(0)
    sheet_content = {}
    for sheet_number_row in range(sheet.nrows):
        sheet_row = sheet.row(sheet_number_row)
        content_key = sheet_row[0].value
        content_value = []
        for row in sheet_row[1:]:
            tmp_value = round(row.value) if isinstance(row.value, float) else row.value
            content_value.append(tmp_value)

        # sheet_content[content_key] = content_value
        sheet_content[content_key] = str(content_value)

    xml_doc = xml.dom.minidom.Document()

    # 创建 xml 根节点
    xml_root = xml_doc.createElement("root")
    xml_doc.appendChild(xml_root)
    # 创建 students 节点并写入学生信息
    student_text = xml_doc.createElement("students")
    student_comment = """<!--
            学生信息表
            "id" : [名字, 数学, 语文, 英文]
        -->"""
    # 当 sheet_content 中含中文时，需要参数 ensure_ascii=False
    student_body = json.dumps(sheet_content, ensure_ascii=False, indent=4)
    student_text.appendChild(xml_doc.createTextNode(student_comment))
    student_text.appendChild(xml_doc.createTextNode(student_body))

    xml_root.appendChild(student_text)

    with open("student.xml", "w") as f:
        f.write(xml_doc.toprettyxml())


if __name__ == "__main__":
    main()
