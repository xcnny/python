# -*- coding:utf-8 -*-
# @author LiuBin
# @date 2025/2/10
# @file 标识符.py
"""
    什么是标识符
    标识符是用来命名变量、函数、类、模块或任何其他对象的名称。
    标识符的命名规则：
    1. 标识符可以由字母（a-z, A-Z）、数字（0-9）、下划线（_）组成，但不能以数字开头。
    2. 标识符是大小写敏感的，即 "Name" 和 "name" 是一个不同的标识符。
    3. 标识符不能使用 Python 关键字或保留字。
    4. 标识符的长度没有限制。
    以下是一些合法的标识符：
    my_name, my_age, _private_var, my_function, MyClass, my_module
"""
my_name = "LiuBin"
my_age = 28
_private_var = "This is a private variable."

def my_function():
    print("This is a function.")
