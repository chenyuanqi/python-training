#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# Created by vikey on 2018/3/7

import sys


def is_prime_number(number):
    """ 判断数值是否为素数

    :param number:
    :return: boolean
    """
    if number <= 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


def location_manieson_number(which_one=1):
    """ 找第 n 个默尼森数

    P 是素数且 M 也是素数，并且满足等式 M = 2**P - 1，则称 M 为默尼森数
    例如，P = 5，M = 2**P - 1 = 31，5 和 31 都是素数，因此 31 是默尼森数

    :param which_one:
    :return:
    """
    p = m = 1
    loop_flag = True
    manieson_number = []

    while loop_flag:
        p += 1

        if not is_prime_number(p):
            continue

        m = 2**p - 1
        if is_prime_number(m):
            manieson_number.append(m)

        if len(manieson_number) == which_one:
            loop_flag = False

    return m


def main(which_one):
    result = location_manieson_number(which_one)
    print(result)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        which_one = int(sys.argv[1])
        main(which_one)
