# -*- coding:utf-8 -*-
# @author LiuBin
# @date 2025/2/11
# @file for循环.py
# name = "itheimal"
# for i in name:
#     # print(i, end='')
#     print(i)


str = "itheima is a brand of itcasting"
sum = 0
for i in str:
    if i == 'a':
        sum += 1
print(f"str 字符产中总共有{sum}个'a'字符")