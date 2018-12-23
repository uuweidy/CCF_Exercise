# -*- coding: utf-8 -*-
"""
给出两个长度分别为n1,n2(n1,n2<=100)且每列高度为1或者2的长条。需要将它们放入一个高度为3的容器，问能够容纳它们的最短容
器长度


Created on 2018/12/12 22:45

@author: 杜雨威
"""
while 1:
    try:
        c = list(map(int, input().replace('\u200b', '')))
        d = list(map(int, input().replace('\u200b', '')))
    except EOFError:
        break
    temp = d
    length = 0
    cnt = 0
    for l in range(len(c)+1):
        if l != 0:
            temp.insert(0, 0)
            cnt += 1
        boolean = True
        for i in range(min(len(c), len(temp))):
            if c[i] + temp[i] > 3:
                boolean = False
                break
        if boolean:
            length = len(temp)
            break
    d = temp[cnt:]
    temp = c
    cnt = 0
    for l in range(len(d)):
        if l != 0:
            temp.insert(0, 0)
            cnt += 1
        boolean = True
        for i in range(min(len(temp), len(d))):
            if temp[i] + d[i] > 3:
                boolean = False
                break
        if boolean:
            if len(temp) < length:
                length = len(temp)
            break
    c = temp[cnt:]
    if length < len(c):
        length = len(c)
    if length < len(d):
        length = len(d)
    print(length)


