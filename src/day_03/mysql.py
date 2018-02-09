#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# Created by vikey on 2018/2/8

from __future__ import print_function
import pymysql


class Mysql(object):
    """ Mysql 操作类

    参考 1：python 风格 sql 查询 -- https://pypi.python.org/pypi/python-sql
    参考 2：面向生成器 sql 接口 -- https://ponyorm.com/

    Attributes:
        __instance: Mysql 单例
        __connection: Mysql 连接
        __cursor：Mysql 游标
    """
    def __new__(cls, **kwargs):
        if not hasattr(cls, '__instance'):
            cls.__instance = super(Mysql, cls).__new__(cls)

        return cls.__instance

    def __init__(self, **kwargs):
        self.__connect(**kwargs)

    def __connect(self, **kwargs):
        """ 连接 Mysql
        Args:
            host: 主机 ip
            user: 用户名
            password: 密码
            database: 数据库名

        Return: None

        Raises:
            pymysql.err.OperationalError
        """
        host = kwargs.get('host', "localhost")
        user = kwargs.get('user', "root")
        password = kwargs.get('password', "root")
        database = kwargs.get('database', "default")

        try:
            self.__connection = pymysql.connect(host=host, user=user, password=password, database=database, charset="utf8")
        except pymysql.err.OperationalError:
            print("connect failed.")
        else:
            self.__cursor = self.__connection.cursor()
        finally:
            pass

    def close(self):
        """ 关闭 Mysql 连接 """
        self.__connection.close()

    def insert(self, table, *args, **kwargs):
        """ 写入 Mysql 数据
        Args:
            table: 表名
            args: 列数据
            kwargs: 字段、数据

        Return:
            last_row_id: 写入 id

        Raises: None
        """
        query = "INSERT INTO `%s` " % table

        if kwargs:
            keys = kwargs.keys()
            values = tuple(kwargs.values())
            query_field = "(" + ",".join(["`%s`"] * len(keys)) % tuple(keys) + ")"
            query_value = " VALUES (" + ",".join(["%s"] * len(values)) + ")"
            query += query_field + query_value
        elif args:
            values = None, args
            query += " VALUES(" + ",".join(["%s"] * len(values)) + ")"
        else:
            values = None

        self.__cursor.execute(query, values)
        self.__connection.commit()

        return self.__cursor.lastrowid

    def update(self):
        pass

    def delete(self):
        pass

    def find(self):
        pass

    def select(self):
        pass


def main():
    mysql_instance = Mysql(host="127.0.0.1", user="ltbl", password="ltbl", database="test")

    with open("keys.txt", "r") as f:
        for data in f.readlines():
            mysql_instance.insert('keys', data.strip())

        # 手动关闭 Mysql 连接
        mysql_instance.close()


if __name__ == '__main__':
    main()
