# -*- coding: utf-8 -*-
"""
输入两个字符串s和t，判断是否可以从t中删除0个或多个字符（其他字符顺序不变），得到字符串s。例如abcde可以得到bce,但无法得到
dc.

Created on 2018/12/11 23:56

@author: 杜雨威
"""
while 1:
    try:
        s, t = map(str, input().strip().split())
    except EOFError:
        break
    temp = t
    is_sub = True
    for c in s:
        if temp.find(c) != -1:
            a = temp.find(c)
            temp = temp[(a+1):]
        else:
            is_sub = False
    if is_sub:
        print('Yes')
    else:
        print('No')
