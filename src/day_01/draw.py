#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# Created by vikey on 2018/2/8

from PIL import Image
from PIL import ImageDraw


def main():
    """
    给图片添加水印
    """
    with Image.open("demo.png") as f:
        draw = ImageDraw.Draw(f)
        draw.text((f.size[0] - 100, 30), "2018-02-08", (255, 0, 0))
        f.save('result.png')


if __name__ == '__main__':
    main()
