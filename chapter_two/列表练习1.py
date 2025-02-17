# -*- coding:utf-8 -*-
# @author LiuBin
# @date 2025/2/13
# @file 列表练习1.py
number = [1,2,3,4,5,6,7,8,9,10]
number_new = []
for i in number:
    if i % 2 == 0:
        number_new.append(i)

print(number_new)

i = 0
while i < len(number):
    if number[i] % 2 == 0:
        number_new.append(number[i])
    i += 1
print(number_new)
