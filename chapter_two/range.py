# -*- coding:utf-8 -*-
# @author LiuBin
# @date 2025/2/13
# @file range.py

"""
range 语法：
range(start, stop[, step])
    功能：生成一个指定范围的数字序列。
    参数：
    - start：起始值，默认为0。
    - stop：结束值，不包含在序列中。
    - step：步长，默认为1。

    注意：
    - start 和 stop 都可以是非整型，但 step 必须是整型。
    - stop 值是 range() 所生成的序列中最后一个元素的下一个值，
        因此，range() 并不包括 stop 值。
    - step 值可以是正数、负数或 0。
    - range() 通常用于循环或迭代。
"""
# 使用示例
for i in range(5):  # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 10):  # 1, 2, 3, 4, 5, 6, 7, 8, 9
    print(i)


for i in range(0, 10, 2):  # 0, 2, 4, 6, 8
    print(i)

for i in range(10, 0, -1):  # 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
    print(i)

# 注意：range() 并不返回一个列表，而是返回一个 range 对象，
# 若需要将 range() 对象的元素生成为列表，可以使用 list() 函数。
print(list(range(5)))  # [0, 1, 2, 3, 4]
print(list(range(1, 10)))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(0, 10, 2)))  # [0, 2, 4, 6, 8]
print(list(range(10, 0, -1)))  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# range() 对象的其他方法
r = range(5)
print(len(r))  # 5
print(r[0])  # 0
print(r[4])  # 4
print(r[-1])  # 4
print(r[5])  # IndexError: range index out of range

# range() 对象的切片
print(r[::2])  # range(0, 5, 2)
print(r[::-1])  # range(4, -1, -1)
print(r[1:4])  # range(1, 4)
print(r[::-2])  # range(4, -1, -2)

# range() 对象的 copy() 方法
r2 = r.copy()
print(r2)  # range(0, 5, 1)

# range() 对象的 count() 方法
print(r.count(1))  # 0
print(r.count(2))  # 1
print(r.count(3))  # 1
print(r.count(4))  # 1
print(r.count(5))  # 1
print(r.count(6))  # 0

# range() 对象的 index() 方法
print(r.index(1))  # 0
print(r.index(2))  # 1
print(r.index(3))  # 2
print(r.index(4))  # 3
print(r.index(5))  # 4
# print(r.index(6))  # ValueError: 6 is not in range(0, 5, 1)