# -*- coding: utf-8 -*-
"""
Created on 2018/12/24 21:52

@author: 杜雨威
"""
while 1:
    cnt = int(input())
    if cnt == 0:
        break
    n = {}
    for i in range(cnt):
        a, b = map(int, input().split())
        if not n.get(a):
            n.update({a: 1})
            # print('新发现一个要转出的学生:', a)
        else:
            n[a] += 1
            # print('发现一个要转出的学生:', a)
        if not n.get(b):
            n.update({b: -1})
            # print('新发现一个要转入的学生:', b)
        else:
            n[b] -= 1
            # print('发现一个要转入的学生:', b)
    can = True
    for i in n.values():
        if i != 0:
            can = False
            break
    if can:
        print('YES')
    else:
        print('NO')

