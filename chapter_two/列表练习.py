# -*- coding:utf-8 -*-
# @author LiuBin
# @date 2025/2/13
# @file 列表练习.py
student_age = [21,25,21,23,22,20]

student_age.append(31)

student_age.extend([29,33,30])

print(student_age)

print(student_age[0])
# pop 方法会改变原列表
first_age = student_age.pop(0)
print(first_age)

last_age = student_age.pop(-1)
print(last_age)

print(student_age.index(31))