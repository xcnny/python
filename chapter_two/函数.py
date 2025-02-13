# -*- coding:utf-8 -*-
# @author LiuBin
# @date 2025/2/11
# @file 函数.py
"""
    函数的概念：
        函数是一段可以被重复使用，并且可以有返回值的代码段。
    函数的格式：
        def function_name(parameter1, parameter2, ...):
            # 函数体
            return value
    函数的类型:
        局部变量和全局变量：
            局部变量：在函数内定义的变量，只在函数内有效。
            全局变量：在函数外定义的变量，在函数内可以直接使用。
            注意：在函数内修改全局变量的值，需要使用global关键字。
        形式参数和实际参数：
            形式参数：在函数定义时定义的参数，在函数内使用。
            实际参数：在函数调用时传递的值，在函数内使用。
        返回值：
            无返回值：在函数体中没有return语句，函数的返回值是None，为空，没有什么实际意义.
            单个返回值：在函数体中只有一行return语句，函数的返回值是return语句的值。
            多个返回值：在函数体中有多行return语句，函数的返回值是最后一个return语句的值。
            注意：在函数中修改局部变量的值，在函数外无法直接使用。
            注意：在函数中返回列表或字典，在函数外可以使用。
            注意：在函数中返回元组，在函数外可以使用。
            注意：在函数中返回函数，在函数外可以使用。
            注意：在函数中返回lambda表达式，在函数外可以使用。
            注意：在函数中返回set，在函数外可以使用。
            注意：在函数中返回frozenset，在函数外可以使用。
            注意：在函数中返回class，在函数外可以使用。
"""
str = "mySession"

def my_function(str):
    count = 0
    for i in str:
        count += 1
    print(count)
my_function(str)

def sum(a,b):
    """
    计算两个数的和
    :param a: 数字1
    :param b: 数字2
    :return: 数字1 + 数字2
    """
    return a + b
sum(4,6)




