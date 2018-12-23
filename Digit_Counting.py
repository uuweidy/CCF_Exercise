# -*- coding: utf-8 -*-
"""
把前n个整数顺次写在一起：123456789101112...数一数0~9各出现多少次
Created on 2018/12/7 22:27

因为这里n < 10000，所以直接使用穷举法

@author: 杜雨威
"""
n = int(input())
num = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
while n != 0:
    s = str(n)
    for i in s:
        num[int(i)] += 1
    n = n - 1
print(num)


