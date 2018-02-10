#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# Created by vikey on 2018/2/9

from __future__ import print_function
from urllib.request import urlopen
from bs4 import BeautifulSoup


def main():
    """ 分析提取 html 链接

    使用 python 3 执行脚本
    bs4 doc: https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html
    """
    html_content = urlopen("https://www.douban.com/")
    bs_instance = BeautifulSoup(html_content, "html.parser")
    links = bs_instance.find_all("a")
    for link in links:
        href_content = link.get("href")
        if href_content:
            print(href_content)


if __name__ == "__main__":
    main()
