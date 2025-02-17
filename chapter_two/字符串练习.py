# -*- coding:utf-8 -*-
# @author LiuBin
# @date 2025/2/13
# @file 字符串练习.py

practice_str = "itheima itcast boxuegu"
print(practice_str.count("it"))
str_new = practice_str.replace(" ","|")
print(str_new)
str_list = str_new.split("|")
print(str_list)