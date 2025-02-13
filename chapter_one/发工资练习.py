# -*- coding:utf-8 -*-
# @author LiuBin
# @date 2025/2/11
# @file 发工资练习.py
import random
money = 10000
i = 1
while i <= 20:
    count = random.randint(1,10)
    if count >= 5:
        print(f"员工{i},绩效分为：{count},发放1000工资")
        money -= 1000
        i += 1
        print(f"账号还剩余余额：{money}")
        if money == 0:
            print(f"账号余额为0")
            break
    else:
        print(f"员工{i},绩效分为：{count},,不发放5工资")
        i += 1
        continue
