# -*- coding:utf-8 -*-
# @author LiuBin
# @date 2025/2/10
# @file if判断.py
"""
    if语句的基本格式：
        if 条件:
            条件成立时执行的代码
    if ... else 语句的基本格式：
        if 条件:
            条件成立时执行的代码
        else :
            条件不成立时执行的代码
"""
age = 30
if age >= 18:
    print("你已成年")


# if...elif...else 语句
score = 85
if score >= 90:
    print("成绩为A")
elif score >= 80:
    print("成绩为B")
elif score >= 70:
    print("成绩为C")
else:
    print("成绩为D")