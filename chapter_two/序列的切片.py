# -*- coding:utf-8 -*-
# @author LiuBin
# @date 2025/2/13
# @file 序列的切片.py
"""
    序列的定义：
    - 序列是一组按特定顺序排列的元素的集合。
    - 序列可以是字符串、列表、元组等。

    切片的语法：
    sequence[start:stop:step]
    start：
        - 起始位置（包括）。
        - 如果不指定，默认为0。
    stop;
        - 结束位置（不包括）。
        - 如果不指定，默认为序列的长度。
    step:
        - 步长。
        - 如果不指定，默认为1。
        - 如果为正值，切片是从左到右。
        - 如果为负值，切片是从右到左。起始下标和结束下标也要反向标注
    切片的应用：
    - 字符串、列表、元组的切片可以用来获取子串或子列表。
    - 切片可以用来修改序列中的元素。
    - 切片可以用来对序列进行排序或反转。

    # 1. 字符串的切片
    string = "Hello, World!"
    print(string[0:5])  # 取前5个字符
    print(string[6:])  # 取从第6个字符开始到结尾的字符
    print(string[2:8:2])  # 取第2到第8个字符，步长为2

    # 2. 列表的切片
    list = ['H', 'e', 'l', 'l', 'o', ',','', 'W', 'o', 'r', 'l', 'd', '!']
    print(list[0:5])  # 取前5个元素
    print(list[6:])  # 取从第6个元素开始到结尾的元素
    print(list[2:8:2])  # 取第2到第8个元素，步长为2

    # 3. 元组的切片
    tuple = ('H', 'e', 'l', 'l', 'o', ',','', 'W', 'o', 'r', 'l', 'd', '!')
    print(tuple[0:5])  # 取前5个元素
    print(tuple[6:])  # 取从第6个元素开始到结尾的元素
    print(tuple[2:8:2])  # 取第2到第8个元素，步长为2

"""

my_list = [0,1,2,3,4,5,6,7,8]
print(my_list[2:5])  # 获取第3到第6个元素,结果为：[2, 3, 4]

test_str = "万过薪月，员序程马黑来，nohtyP学"
new_str = test_str[5:10]
new_str1 = new_str[::-1]
print(new_str1)  # 黑马程序员