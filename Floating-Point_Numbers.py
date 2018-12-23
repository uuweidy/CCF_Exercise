# -*- coding: utf-8 -*-
"""

说实话没看懂题

思路来自：https://www.cnblogs.com/SuuT/p/9451892.html
直接暴力循环找答案
Created on 2018/12/12 23:10

@author: 杜雨威
"""
from math import log

while 1:
    a, b = map(float, input().split('e'))
    if a == 0 and b == 0:
        break
    is_over = False
    a = log(a) + b * log(10)
    for i in range(1, 31):
        if is_over:
            break
        for j in range(0, 10):
            m, e = 0, 0
            for k in range(0, j+1):
                m += 1
                m /= 2
            for l in range(1, i+1):
                e *= 2
                e += 1
            if abs(a - log(m) - e * log(2)) < 1e-4:  # ?为什么1e-7会是WA?
                print(str(j)+' '+str(i))
                is_over = True
                break


