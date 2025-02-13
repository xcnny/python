# -*- coding:utf-8 -*-
# @author LiuBin
# @date 2025/2/10
# @file 类型转换.py
"""
类型之间的转换：
    int()：将其他数据类型转换成整型  浮点数转化为整数会丢失精度
    float()：将其他数据类型转换成��点数
    str()：将其他数据类型转换成字符串
    bool()：将其他数据类型转换成布尔值
    list()：将其他数据类型转换成列表
    dict()：将其他数据类型转换成字典
    tuple()：将其他数据类型转换成元组
    set()：将其他数据类型转换成集合
    complex()：将其他数据类型转换成复数
    chr()：将 ASCII 值转换成字符
    ord()：将字符转换成 ASCII 值
    eval()：将字符串转换成 Python 表达式
"""
# 数字类型转换为字符串
print(str(123))  # 123
print(str(123.456))  # 123.456
print(str(-123))  # -123
# 将字符串转换为数字
print(int('123'))  # 123
print(int('123.456'))  # 123
print(int('-123'))  # -123
print(float('123'))  # 123.0
print(float('123.456'))  # 123.456
print(float('-123'))  # -123.0
# 整数转换为浮点数
print(float(123))  # 123.0
print(float(-123))  # -123.0