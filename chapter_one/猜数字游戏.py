# -*- coding:utf-8 -*-
# @author LiuBin
# @date 2025/2/11
# @file 猜数字游戏.py
import random
num1 = random.randint(1,100)
# print(num1)
i = 0
while True:
    guess = input("请输入你要猜的数字：")
    guess = int(guess)
    i += 1
    if guess == num1:
        print(f"恭喜你，猜对了！你总共猜了{i}次。")
        break
        # ��对了，结束循环
        # break ���ر�������
        # continue ���ر��������е���
    elif guess >= num1:
        print("你猜大了")
    else:
        print("你猜小了")