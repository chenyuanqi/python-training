#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# Created by vikey on 2018/2/9

from __future__ import print_function
from HTMLParser import HTMLParser
import urllib


class BodyParser(HTMLParser):
    """ 分析提取 html body (使用 BeautifulSoup 更佳)

    handle_starttag: 要分析的开始标签
    handle_data: 分析 html
    handle_endtag: 要分析的解析标签
    """
    def __init__(self):
        self.body = ""
        self.is_body = False
        HTMLParser.__init__(self)

    def handle_starttag(self, tag, attributes):
        if tag == 'body':
            self.is_body = True

    def handle_data(self, data):
        if self.is_body:
            self.body += data

    def handle_endtag(self, tag):
        if tag == 'body':
            self.is_body = False


def main():
    url = "http://www.baidu.com/"
    html_instance = urllib.urlopen(url)
    html_content = html_instance.read()

    parser = BodyParser()
    parser.feed(html_content)
    print(parser.body)


if __name__ == '__main__':
    main()
