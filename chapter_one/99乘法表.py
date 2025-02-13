# -*- coding:utf-8 -*-
# @author LiuBin
# @date 2025/2/11
# @file 99乘法表.py
# 打印输出99乘法表
"""
def print_multiplication_table(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(f"{i}*{j} = {i*j:2}", end="\t")
            print()
"""
# for i in range(1,10):
#     for j in range(1, i+1):
#         print(f"{j}*{i} = {i*j:2}", end="\t")
#     print()

i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f"{j}*{i} = {i*j:2}", end="\t")   # 打印输出中 i*j 结果的最小字段宽度为2
        j += 1
    print()
    i += 1

# i = 1
# while i <= 9:
#     j = 1
#     while j <= i:
#         print(f"{j}*{i} = {i*j}\t", end='')
#         j += 1
#     print()   # 打印换行符
#     i += 1