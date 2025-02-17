# -*- coding:utf-8 -*-
# @author LiuBin
# @date 2025/2/17
# @file 数据容器通用操作.py
# 定义一个列表
my_list = [1, 2, 3, 4, 5]
# 定义一个元祖
my_tuple = (1, 2, 3, 4, 5)
# 定义一个字符串
my_string = "Hello, World!"
# 定义一个集合
my_set = {1, 2, 3, 4, 5}
# 定义一个字典
my_dict = {"name": "LiuBin", "age": 25}

# 数据容器转列表
list_from_tuple = list(my_tuple)
list_from_string = list(my_string)
list_from_set = list(my_set)
list_from_dict = list(my_dict)
print(list_from_dict)   # ['name', 'age']
print(list_from_string)
print(list_from_set)
print(list_from_tuple)
print("----------------------------------------")
# 数据容器转元祖
tuple_from_list = tuple(my_list)
tuple_from_string = tuple(my_string)
tuple_from_set = tuple(my_set)
tuple_from_dict = tuple(my_dict)
tuple_from_dict_value = tuple(my_dict.values())
print(tuple_from_dict)   # ('name', 'age')
print(tuple_from_dict_value)   # ('LiuBin', 25)
print(tuple_from_string)
print(tuple_from_set)
print(tuple_from_list)
print("----------------------------------------")
# 数据容器转集合
set_from_list = set(my_list)
set_from_string = set(my_string)
set_from_tuple = set(my_tuple)
set_from_dict = set(my_dict.items())
print(set_from_dict)   # {'name', 'age'}
print(set_from_string)
print(set_from_tuple)
print(set_from_list)
print("----------------------------------------")
# 数据容器转字典
# dict_from_list = dict(my_list)
# dict_from_string = dict(my_string)
# dict_from_tuple = dict(my_tuple)
dict_from_dict = dict(my_dict)
print(dict_from_dict)   # {'name': 'LiuBin', 'age': 25}
# print(dict_from_string)

