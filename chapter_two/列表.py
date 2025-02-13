# -*- coding:utf-8 -*-
# @author LiuBin
# @date 2025/2/12
# @file 列表.py
"""
    列表的语法：
    - 列表是由一系列元素组成的有序集合。
    - 列表是可以修改的，可以添加、删除元素。
    - 列表是用方括号 [] 定义的。
    - 列表中的元素可以是任何数据类型，可以是不同的数据类型，支持嵌套
    - 列表中的元素可以是任意数据类型，包括：整型、字符串、布尔值、列表、元组、字典等

    # 1. 创建列表
    list1 = ['apple', 'banana', 'cherry']
    list2 = list('hello')
    # 定义空列表
    list3 = []
    list4 = list()

    # 2. 列表元素的访问
    print(list1[0])  # 输出：apple
    print(list2[1])  # 输出：e

    # 3. 列表元素的修改
    list1[0] = 'orange'
    print(list1)  # 输出：['orange', 'banana', 'cherry']

    # 4. 列表元素的添加
    list1.append('grape')
    print(list1)  # 输出：['orange', 'banana', 'cherry', 'grape']

    # 5. 列表元素的删除
    del list1[2]
    print(list1)  # 输出：['orange', 'banana', 'grape']

    list1.remove('banana')
    print(list1)  # 输出：['orange', 'grape']

    # 2. 列表元素的访问
    print(list1[0])  # 输出：apple
    print(list2[1])  # 输出：e

    # 3. 列表元素的修改
    list1[0] = 'orange'
    print(list1)  # 输出：['orange', 'banana', 'cherry']

    # 4. 列表元素的添加
    list1.append('grape')
    print(list1)  # 输出：['orange', 'banana', 'cherry', 'grape']

    # 5. 列表元素的删除
    del list1[2]
    print(list1)  # 输出：['orange', 'banana', 'grape']

    list1.remove('banana')
    print(list1)  # 输出：['orange', 'grape']

    # 6. 列表元素的切片
    print(list1[1:3])  # 输出：['grape', 'orange']
    print(list1[:2])  # 输出：['orange', 'grape']
    print(list1[2:])  # 输出：['grape']

    # 7. 列表元素的拼接
    list3 = list1 + ['kiwi', 'mango']
    print(list3)  # 输出：['orange', 'grape', 'kiwi','mango']

    # 8. 列表元素的拼接
    list4 = ['pear'] * 3
    print(list4)  # 输出：['pear', 'pear', 'pear']

    # 9. 列表元素的排序
    list5 = ['apple', 'banana', 'cherry', 'orange']
    list5.sort()
    print(list5)  # 输出：['apple', 'banana', 'cherry', 'orange']

    list5.reverse()
    print(list5)  # 输出：['orange', 'cherry', 'banana', 'apple']

    # 10. 列表元素的��贝
    list6 = list5.copy()
    print(list6)  # 输出：['orange', 'cherry', 'banana', 'apple']

    # 11. 列表元素的统计
    print(list5.count('apple'))  # 输出：1

    # 12. 列表元素的推导
    list7 = [i for i in range(10) if i % 2 == 0]
    print(list7)  # 输出：[0, 2, 4, 6, 8]

    # 13. 列表元素的��套
    list8 = [['apple', 'banana'], ['cherry', 'orange']]
    print(list8[0][0])  # 输出：apple

    # 14. 列表元素的��套
    list9 = [i for sublist in list8 for i in sublist]
    print(list9)  # 输出：['apple', 'banana', 'cherry', 'orange']

    # 15. 列表元素的��套
    list10 = [[i for i in range(j)] for j in range(1, 6)]
    print(list10)  # 输出：[[0], [0, 1], [0, 1, 2], [0, 1, 2, 3], [0, 1, 2, 3, 4]]

    # 16. 列表元素的��套
    list11 = [i for i in range(10) if i % 2 == 0 if i % 3 == 0]
    print(list11)  # 输出：[0]

    # 17. 列表元素的��套
    list12 = [i for i in range(10) if i % 2 == 0 if i % 3 == 0 if i % 5 == 0]
    print(list12)  # 输出：[]

    # 18. 列表元素的��套
    list13 = [i for i in range(10) if i % 2 == 0 if i % 3 == 0 if i % 5!= 0]
    print(list13)  # 输出：[1, 2, 4, 7]
"""
# 定义列表
name_list = ["itheima","itcast","python",666,True,["python",123,"Java"]]
print(name_list)
print(type(name_list))

# 列表元素的访问，通过下标索引访问
print(name_list[0])
print(name_list[1])
print(name_list[2])
print(name_list[-1][2])

# 反向索引
print(name_list[-1])
print(name_list[-2])
print(name_list[-3])

# 列表元素的修改
name_list[2] = "C++"
print(name_list)

# 列表元素添加
name_list.append("Go")
print(name_list)

# 列表元素的删除
# del name_list[2]
# print(name_list)
# 列表元素的取出和删除
element = name_list.pop(3)
print(element)
print(name_list)
# 指定元素内容删除
# name_list.remove("Go")
# print(name_list)

# 列表元素的切片
# name_list = ["itheima","itcast","C++",666,True,["python",123,"Java"],"Go"]
print(name_list[1:3])   # ['itcast', 'C++']
print(name_list[:2])    # ['itheima', 'itcast']
print(name_list[2:])    # ['C++', 666, True, ['python', 123, 'Java'], 'Go']

# 查找元素的在列表内的下表索引
print(name_list.index("C++"))  # 2


# 特定索引位置插入元素
name_list.insert(2, "GoHome")
print(name_list)

# 在列表尾部追加一批元素
name_list.extend(["传智教育", "JavaScript"])
print(name_list)

# 清空列表
# name_list.clear()
# print(name_list)

# 统计元素在列表中的出现次数
name_list.count("Java")

# 统计列表内有多少个元素
print(len(name_list))

# 列表的遍历
i = 0
# while循环
while i < len(name_list):
    print(name_list[i])
    i += 1
# for 循环
for i in range(0,len(name_list)):
    print(name_list[i])

for element in name_list:
    print(element)
