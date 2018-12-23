# -*- coding: utf-8 -*-
"""
如果一个字符串可以由某个长度为k的字符串重复多次得到，则称该串以k为周期。输入一个长度不超过80的字符串，输出其最小周期

Created on 2018/12/10 20:50

@author: 杜雨威
"""
for cnt in range(int(input())):
    string = str(input())
    if string == '':
        string = str(input())
    if cnt != 0:
        print()
    length = len(string)
    a = []
    for i in range(length + 1):
        if length % (i + 1) == 0:
            a.append(i + 1)
    m = 0
    for i in a:
        k = string[0:i]
        temp = ''
        for j in range(int(length / i)):
            temp += k
        if temp == string:
            m = i
            break
    print(m)

