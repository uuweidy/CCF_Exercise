# -*- coding: utf-8 -*-
"""
Created on 2018/12/24 21:15

@author: 杜雨威
"""
while 1:
    num = int(input())
    if num == 0:
        break
    n = [i for i in range(1, num + 1)]
    print("Discarded cards:", end="")
    boolean = True
    while len(n) != 1:
        if boolean:
            boolean = False
            print(' ',end='')
        else:
            print(', ', end='')
        print(n.pop(0), end='')
        if len(n) != 1:
            n.append(n.pop(0))
        else:
            break
    print()
    print('Remaining card: ' + str(n[0]))


