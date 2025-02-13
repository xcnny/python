# -*- coding:utf-8 -*-
# @author LiuBin
# @date 2025/2/10
# @file 数据输入.py
"""
    数据输入：input
    功能：让用户在键盘上输入一些数据
    接收的内容为字符产类型
"""
from email.charset import add_codec

name = input("请输入你的名字：")
print(type(name))
print(f"你好，{name}!")