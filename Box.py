# -*- coding: utf-8 -*-
"""
给定6个矩形的长和宽wi和hi(1<=wi,hi<=1000)，判断它们能否构成长方体的6个面

Created on 2018/12/12 21:47

@author: 杜雨威
"""
while 1:
    a = {}
    w = 0
    h = 0
    is_tangle = True
    is_over = False
    for i in range(6):
        try:
            w, h = input().split()
        except EOFError:
            is_over = True
            break
        if w > h:
            w, h = h, w
        if (w, h) in a:
            a[(w, h)] += 1
        else:
            a[(w, h)] = 1
    if is_over:
        break

    for i in a.values():
        if i != 2 and i != 4 and i != 6:
            is_tangle = False
            break

    if is_tangle:
        c = 0
        if len(a) == 1:
            if w == h:
                pass
            else:
                is_tangle = False
        elif len(a) == 2:
            for k in a.keys():
                if a[k] == 2:
                    if k[0] != k[1]:
                        is_tangle = False
                        break
                    else:
                        c = k[0]
                else:
                    w = k[0]
                    h = k[1]
            if is_tangle and (c == w or c == h):
                pass
        else:
            b = []
            for w, h in a:
                if a[(w, h)] == 2:
                    b.append([w, h])
                else:
                    b.append([w, h])
                    b.append([w, h])
            if b[0][0] == b[1][0]:
                if b[0][1] == b[2][0]:
                    if b[1][1] == b[2][1]:
                        pass
                    else:
                        is_tangle = False
                elif b[0][1] == b[2][1]:
                    if b[1][1] == b[2][0]:
                        pass
                    else:
                        is_tangle = False
                else:
                    is_tangle = False
            elif b[0][0] == b[1][1]:
                if b[0][1] == b[2][0]:
                    if b[1][0] == b[2][1]:
                        pass
                    else:
                        is_tangle = False
                elif b[0][1] == b[2][1]:
                    if b[1][0] == b[2][0]:
                        pass
                    else:
                        is_tangle = False
                else:
                    is_tangle = False
            elif b[0][0] == b[2][0]:
                if b[0][1] == b[1][0]:
                    if b[1][1] == b[2][1]:
                        pass
                    else:
                        is_tangle = False
                elif b[0][1] == b[1][1]:
                    if b[2][1] == b[1][0]:
                        pass
                    else:
                        is_tangle = False
                else:
                    is_tangle = False
            elif b[0][0] == b[2][1]:
                if b[0][1] == b[1][0]:
                    if b[1][1] == b[2][0]:
                        pass
                    else:
                        is_tangle = False
                elif b[0][1] == b[1][1]:
                    if b[1][0] == b[2][0]:
                        pass
                    else:
                        is_tangle = False
                else:
                    is_tangle = False
            else:
                is_tangle = False

    if is_tangle:
        print('POSSIBLE')
    else:
        print('IMPOSSIBLE')
