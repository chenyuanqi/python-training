#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# Created by vikey on 2018/3/6

from PIL import Image
import pytesseract
import sys


def read_image(image_path):
    """ 读取图片内容 (识别效果不太理想)
        Args:
            image_path: 图片路径

        Return: string

        Raises: None

        Dependence:
            pip install PIL
            pip install pytesseract

            系统需要安装识别引擎及中文语言包
            apt-get install tesseract-ocr
            apt-get install tesseract-ocr-chi-sim

        Optimize:
            推荐腾讯云图像识别 https://cloud.tencent.com/document/product/641/12440
    """
    image_instance = Image.open(image_path)
    image_string = pytesseract.image_to_string(image_instance, lang="chi_sim")

    return image_string


def main(image_path):
    print(read_image(image_path))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("The picture path is required.")
