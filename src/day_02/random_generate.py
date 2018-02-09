#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# Created by vikey on 2018/2/8


import random


def generate_code(number):
    result = set()

    try:
        for n in range(number):
            result.add(str(random.randint(10000000, 99999999)))
    except ValueError as e:
        print(e)
    finally:
        while number != len(result):
            result_append = generate_code(number - len(result))
            result = result | result_append

        return result


def main():
    with open("keys.txt", "w") as f:
        keys = generate_code(200)

        f.write("\n".join(list(keys)))


if __name__ == '__main__':
    main()
