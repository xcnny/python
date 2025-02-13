# -*- coding:utf-8 -*-
# @author LiuBin
# @date 2025/2/10
# @file while 循环.py
"""
while 循环语句：
    while 条件:
        代码块

"""
i = 0
sum = 0
while i <= 100:
    # print(f"i 的值是 {i}")
    sum += i
    i += 1
print(f"0到100的累加之和为：{sum}")
print("0到100的累加之和为：%s" % sum)