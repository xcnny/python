# -*- coding:utf-8 -*-
# @author LiuBin
# @date 2025/2/17
# @file 集合.py
"""
集合的定义：
- 集合是由一组无序且不重复元素组成的,不支持下表索引
- 集合中的元素是不可变的
- 集合的创建：
  - 空集合：set()
  - 集合的字面量：{1, 2, 3, 4, 5}
集合的特点：
  - 集合是无序的
  - 集合中的元素是不允许重复的
  - 集合中的元素是可以是任何不可变的数据类型
  -



"""
my_set = {"传智教育","黑马程序员","传智教育","黑马程序员","传智教育","黑马程序员","传智教育","黑马程序员",}
my_empty_set = set()
print(my_set,type(my_set))   # 结果为：{'黑马程序员', '传智教育'} <class 'set'>
print(my_empty_set,type(my_empty_set))
# 添加元素
my_set.add("Python")
my_set.add("Java")
print(my_set)  # 结果为：{'黑马程序员', 'Python', 'Java', '传智教育'}

# 删除元素
my_set.remove("黑马程序员")
print(my_set)  # 结果为：{'Python', 'Java', '传智教育'}
my_set.discard("C++")  # 元素不存在不报错
print(my_set)  # 结果为：{'Python', 'Java', '传智教育'}

# 随机取出一个元素
print(my_set.pop())  # 结果为：Python
print(my_set)  # 结果为：{'Java', '传智教育'}

# 清空集合
my_set.clear()
print(my_set)  # 结果为：set()

# 取两个集合的差集，集合1有而集合2没有的，会得到一个新的集合，集合1和集合2不变
my_set1 = {"Python", "Java", "C++", "Go"}
my_set2 = {"Python", "Java", "JavaScript", "Go"}
print(my_set1 - my_set2)  # 结果为：{'C++'}

my_set3 = my_set1.difference(my_set2)
print(my_set3)  # 结果为：{'C++'}

# 消除两个集合的差集，对比集合1和集合2，在集合1内，删除和集合2相同的元素，最终结果是集合1被修改，集合2不变
my_set1.difference_update(my_set2)
print(my_set1)  # 结果为：{'C++'}
print(my_set2)

# 集合的合并，将集合1和集合2组合成新集合，集合1和集合2不变
my_set1 = {"Python", "Java", "C++", "Go"}
my_set2 = {"Python", "Java", "JavaScript", "Go"}
print(my_set1 | my_set2)  # 结果为：{'C++', 'Go', 'Java', 'JavaScript', 'Python'}

my_set3 = my_set1.union(my_set2)
print(my_set3)  # 结果为：{'C++', 'Go', 'Java', 'JavaScript', 'Python'}

# 统计集合的元素
my_set4  = {"Python", "Java", "C++", "Go"}
print(len(my_set4))  # 结果为：4

# 集合的遍历,不支持while循环
my_set5  = {"Python", "Java", "C++", "Go"}
for i in my_set5:
    print(i)

# 集合的交集,取两个集合一样的元素，得到一个新集合，原集合不变
my_set1 = {"Python", "Java", "C++", "Go"}
my_set2 = {"Python", "Java", "JavaScript", "Go"}
print(my_set1 & my_set2)  # 结果为：{'Java', 'Go', 'Python'}

my_set3 = my_set1.intersection(my_set2)
print(my_set3)  # 结果为：{'Java', 'Go', 'Python'}

print(my_set1)
print(my_set2)

