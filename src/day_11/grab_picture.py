#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# Created by vikey on 2018/2/10

from __future__ import print_function
import os
import re
import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup


def get_image_url(url):
    """ 分析提取 image 链接
    Args:
        url: 要抓取的 url

    Return: list(所有图片链接)

    Raises: None
    """
    html_content = urlopen(url)
    bs_instance = BeautifulSoup(html_content, "html.parser")
    links = bs_instance.find_all("img")
    result = []

    for link in links:
        href_content = link.get("src")
        if href_content:
            result.append(href_content)

    return list(set(result))


def download_image(url, dir_name="download"):
    """ 分析提取 image 链接
    Args:
        url: 要下载的 url
        dir_name: 保存图片目录

    Return: 保存图片到指定目录

    Raises: mkdir Failed
    """
    try:
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)
    except BaseException:
        print("Failed to create directory for download image.")
        exit()

    for pic_url in url:
        # 链接无效，则执行下一轮
        if not re.match(r'^https?:/{2}\w.+$', pic_url):
            continue

        pic_data = urllib.request.urlopen(pic_url).read()
        pic_name = re.split("/", pic_url)[-1]

        # 图片名过长，截取后 80 个字符
        if len(pic_name) > 80:
            pic_name = pic_name[-80:]

        pic_path = dir_name + "/" + pic_name

        with open(pic_path, "wb") as f:
            f.write(pic_data)


def main():
    target_link = "http://tieba.baidu.com/p/2166231880"
    grab_links = get_image_url(target_link)
    download_image(grab_links)


if __name__ == "__main__":
    main()
