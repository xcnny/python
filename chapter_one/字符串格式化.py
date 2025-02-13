# -*- coding:utf-8 -*-
# @author LiuBin
# @date 2025/2/10
# @file 字符串格式化.py
"""
字符产格式化

Python 3.6 引入了 f-string 格式化，使得字符串格式化更加方便。

f-string 是一个用在引号内的字符串，用大括号 {} 包含的表达式来进行格式化。
f-string 格式化可以让代码更具可读性，并且在某些场景下可以提高性能。
f-string 格式化示例：

"""
# f"{变量}" 不会进行精度控制
name = "Alice"
age = 25
print(f"Hello, {name}! Your age is {age}.")
# 使用%s占位字符穿，通过%d占位整数，通过%f占位浮点数
name = "黑马程序员"
message = "学IT就来 %s" % name
print(message)
# 多个变量占位，变量要用括号括起来，并按照占位的顺序填入
class_num = 57
avg_salary = 16781
message = "Python 大数据学科，北京%s期，毕业平均工资：%s" % (class_num, avg_salary)
print(message)

num1 = 11
num2 = 11.345
print("num2的数字宽度限制为4，精度限制为2，结果是：%4.2f" % num2)

