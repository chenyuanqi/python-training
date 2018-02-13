#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
# Created by vikey on 2018/2/13

from __future__ import unicode_literals
from __future__ import print_function
import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import re
import sys
import os


class Spider(object):
    def __init__(self, url=""):
        url_info = urlparse(url)
        self.url = url
        self.main_url = url_info.scheme + "://" + url_info.netloc

    def crawl(self):
        """ 分析抓取视频页链接
        Args: None

        Return: list(所有无重复链接)

        Raises: None
        """
        html_content = urlopen(self.url)
        bs_instance = BeautifulSoup(html_content, "html.parser")
        links = bs_instance.select(".video-box a")
        result = []

        for link in links:
            href_content = link.get("href")
            if not re.match(r'^https?:/{2}\w.+$', href_content):
                href_content = self.main_url + href_content

            result.append(href_content)

        return list(set(result))

    @classmethod
    def download(cls, url, download_dir="rails365"):
        """ 下载视频（先分析视频链接）
        TODO：
            使用多线程处理

        Args:
            url: 下载页所有链接
            download_dir: 下载目录

        Return: None

        Raises:
            BaseException： 创建目录失败
        """
        try:
            if not os.path.exists(download_dir):
                os.mkdir(download_dir)
        except BaseException:
            print("Failed to create directory for download video.")
            exit()

        for download_url in url:
            html_content = urlopen(download_url)
            bs_instance = BeautifulSoup(html_content, "html.parser")
            video_list = bs_instance.select("video")
            if len(video_list):
                video_url = video_list[0].get("src")
                video_name = re.split("/", video_url)[-1]
                video_path = download_dir + "/" + urllib.parse.unquote(video_name)
                video_data = urllib.request.urlopen(video_url).read()

                with open(video_path, "wb") as f:
                    f.write(video_data)


def main(rails365_url="", is_download=False):
    rails365_spider = Spider(rails365_url)
    video_links = rails365_spider.crawl()
    if is_download:
        rails365_spider.download(video_links)
    else:
        for video_link in video_links:
            print(video_link)


if __name__ == "__main__":
    if sys.argv[1] and re.match(r'^https?:/{2}\w.+$', sys.argv[1]):
        is_download = len(sys.argv) > 2 and sys.argv[2]
        main(sys.argv[1], is_download)
    else:
        print("parameter url is required.")
