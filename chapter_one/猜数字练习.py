# -*- coding:utf-8 -*-
# @author LiuBin
# @date 2025/2/10
# @file 猜数字练习.py
import random

print(" 猜数字游戏")
print("我在1-100之间随机选择一个数字，请你来 猜")

# 随机生成一个1-100的数字
num = random.randint(1, 100)

# 开始 猜数字
while True:
    # 请用户输入一个数字
    guess = int(input("请输入数字："))

    # 判断输入的数字是否正确
    if guess == num:
        print("恭喜你， 猜对了!")
        break
    elif guess > num:
        print("大了，请再 猜小一点!")
    else:
        print("小了，请再 猜大一点!")
