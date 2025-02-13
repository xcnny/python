# -*- coding:utf-8 -*-
# @author LiuBin
# @date 2025/2/11
# @file range.py
"""
range()函数返回一个可迭代的序列，一般用在 for 循环中。
    range(start, stop[, step])
        start: 计数从 start 开始。默认是 0
        stop: 计数到 stop 但不包括 stop。
        step: 步长，默认为 1。如果为负数，则为倒序。
"""
print(range(0,9))
print(list(range(0,9)))  # 默认步长为1
print(list(range(0,9,2)))  # 设置步长为2
print(list(range(5,9,2)))
print(list(range(0,9,-1)))  # 输出为[]
# 倒序排列
print(list(range(9,0,-1)))
print(list(range(9,0,-2)))

# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{j}*{i}={j*i:2}", end="\t")
#         j +=1
#     print()
#     i += 1