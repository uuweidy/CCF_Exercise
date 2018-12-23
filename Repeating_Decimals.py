# -*- coding: utf-8 -*-
"""
输入整数a和b（0<=a<=3000,1<=b<=3000），输出a/b的循环小数表示以及循环节长度。例如a=5,b=43,小数表示为
0.(116279069767441860465)，循环节长度为21.

Created on 2018/12/11 23:16

@author: 杜雨威
"""
while 1:
    try:
        a, b = map(int, input().strip().split())
    except EOFError:
        break
    m, n = a, b
    pos = []
    i = 0
    start, end = 0, 0
    zhengshu = int(a / b)
    mod = a % b
    while 1:
        is_end = False
        a = mod * 10
        k = int(a / b)
        mod = a % b
        i += 1
        for j in pos:
            if j[0] == k and j[1] == mod:
                start = j[2]
                end = i
                pos.append([k, mod, i])
                is_end = True
                break
        if is_end:
            break
        pos.append([k, mod, i])

    s = str(zhengshu) + '.'
    for k in range(end - 1):
        if pos[k][2] == start:
            s += '('
        s += str(pos[k][0])
        if pos[k][2] == end-1:
            s += ')'
    if end - start >= 50:
        s = s[:(52+len(str(zhengshu)))] + '...' + ')'
    print(str(m) + '/' + str(n) + ' = ' + s)
    print('   ' + str(end-start) + ' = number of digits in repeating cycle')
    print()
