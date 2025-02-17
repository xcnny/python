# -*- coding:utf-8 -*-
# @author LiuBin
# @date 2025/2/17
# @file 集合练习.py
my_list = ["黑马程序员","传智博客","黑马程序员","传智博客","ITheima","itcast","ITheima","itcast"]
my_set = set()
for item in my_list:
    my_set.add(item)
print(my_set)

i = 0
while i < len(my_list):
    my_set.add(my_list[i])
    i += 1
print(my_set)