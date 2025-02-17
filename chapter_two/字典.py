# -*- coding:utf-8 -*-
# @author LiuBin
# @date 2025/2/17
# @file 字典.py
"""
字典的定义：
    字典是Python中另一个内置的数据类型，它是一个无序的键值对集合。
    字典是由键和值组成的元素，并使用大括号 {} 定义。
    键-值对用封号 : 分隔，键-值对之间用逗号 , 分隔。
    字典的键必须是不可变的数据类型，如字符串、数字或元组，而值可以是任意数据类型。
    字典是一种高效的数据结构，可以用键来快速查询值。
    字典是不允许有重名键的，如果键相同，后面的键值对会覆盖前面的键值对。
    字典的键和值可以是任何 Python 对象。
字典的语法：
    dict = {key1: value1, key2: value2, ...}
    键-值对用��号分隔，键-值对之间用��号 : 分隔。
        例如：
        dict = {'name': 'John', 'age': 25, 'city': 'New York'}
        也可以使用 dict() 函数来创建字典。

"""
# 定义空字典
dict1 = {}
my_dict = dict()
print(dict1)
print(my_dict)
dict2 = {'name': 'John', 'age': 25, 'city': 'New York'}
print(dict2, type(dict2))

# 定义重复key的字典
dict3 = {'name': 'John', 'name': 'Mary', 'age': 25, 'age': 30}
print(dict3)  # 结果为：{'name': 'Mary', 'age': 30}

# 从字典中基于key获取value
print(dict2['name'])  # 结果为：John
print(dict2['age'])  # 结果为：25

# 生成一个学生成绩嵌套字典
students = {'Alice':
                {'math': 85,
                 'english': 92,
                 'chinese': 90},
            'Bob':
                {'math': 90,
                 'english': 88,
                 'chinese': 95},
            'Charlie':
                {'math': 88,
                 'english': 95,
                 'chinese': 85}}
print(students)
print(students["Bob"]['math'])
# 新增元素
students["David"] = {'math': 95, 'english': 90, 'chinese': 88}
print(students)
# 删除元素
del students["David"]
print(students)

Bon = students.pop("Bob")
print(Bon)
print(students)

# 字典的键值对修改
dict4 = {'name': 'John', 'age': 25, 'city': 'New York'}
dict4['name'] = 'Mary'
print(dict4)

# 清空字典
dict5 = {'name': 'John', 'age': 25, 'city': 'New York'}
dict5.clear()
print(dict5)

# 字典的键值对��贝
dict6 = {'name': 'John', 'age': 25, 'city': 'New York'}
dict7 = dict6.copy()
print(dict7)

# 字典的键值对��接
dict8 = {'name': 'John', 'age': 25, 'city': 'New York'}
dict9 = {'gender': 'Male', 'hobby': 'Reading'}
dict8.update(dict9)
print(dict8)

# 字典的键值对排序
dict10 = {'name': 'John', 'age': 25, 'city': 'New York'}
# sorted_dict = dict(sorted(dict10.items(), key=lambda x: x[1]))
# print(sorted_dict)

# 字典的键值对反转
# reversed_dict = dict(reversed(sorted(dict10.items(), key=lambda x: x[1])))
# print(reversed_dict)

# 字典的键值对查询
print('name' in dict10)  # 结果为：True
print('job' in dict10)  # 结果为：False

# 字典的键值对计数
print(len(dict10))  # 结果为：3

# 字典的键值对迭代
# for key, value in dict10.items():
#     print(key, value)
keys = dict10.keys()
for key in keys:
    print(key, dict10[key])

for key in dict10:
    print(key, dict10[key])

# 字典的键值对转换
tuple_dict = dict(zip(['name', 'age', 'city'], ['John', 25, 'New York']))
print(tuple_dict)

# 获取全部key
print(dict10.keys())

# 获取全部value
print(dict10.values())