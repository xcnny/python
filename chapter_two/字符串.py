# -*- coding:utf-8 -*-
# @author LiuBin
# @date 2025/2/13
# @file 字符串.py
"""
字符串的相关操作：
1. 字符串拼接
2. 字符串截取
3. 字符串截取子串
4. 字符串截取子串并修改
5. 字符串截取子串并翻转
7. 字符串截取子串并去重
8. 字符串截取子串并去重并排序
9. 字符串中字符的统计
10. 字符串中字符的位置
11. 字符串中字符的反转
12. 字符串中字符的排序
13. 字符串中字符的替换

"""
# 字符串的定义
my_str = "Itheima and itcast"
# 下标
value = my_str[2]
value2 = my_str[-16]
print(value)  # 输出: h
print(value2)  # 输出: h
# index 方法
index = my_str.index("and")
print(index)  # 输出: 8

# 字符串修改/删除
# my_str[2] = "H"   # TypeError: 'str' object does not support item assignment
# replace 方法，得到的是一个新的字符串，并没有改变原字符串
str_new = my_str.replace("it","IT")
print(str_new)  # 输出: Itheima and ITcast

# split 方法，按照指定的分隔符分割字符串，将字符串划分为多个字符串，并存入列表对象中
str_list = my_str.split(" ")
print(str_list)  # 输出: ['Itheima', 'and', 'itcast']

# 字符串的规整操作，默认去除前后空格以及回车符，传参就是去除指定的字符串，每个字符都会被移除
my_str1 = " itheima and itcast "
str_new1 = my_str1.strip()
print(str_new1) #

my_str2 = " itheima and itcast\n"
str_new2 = my_str2.strip()
print(str_new2) # 输出: itheima and itcast

my_str3 = "12itheima and itcast21"
str_new3 = my_str3.strip("12")
print(str_new3) # 输出: itheima and itcast

# 统计字符串中字符的出现次数
print(str_new.count("It"))
# 统计字符串的长度
print(len(str_new))
# 字符串的拼接
str_new4 = " " + str_new + " "
print(str_new4)
# 字符串的翻转
str_new5 = my_str[::-1]
print(str_new5) # 结果：tsacti dna amiehtI

# 替换操作
str_new6 = my_str.replace("and", "and_new")
print(str_new6) # 输出: Itheima and_new ITcast

