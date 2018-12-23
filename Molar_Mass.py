# -*- coding: utf-8 -*-
"""
给出一种物质的分子式，求分子量。本体的分子式中只包含四种原子，分别为CHON，原子量分别为12.01,1.008,16.00,14.01。
例如，C6H5OH的分子量为94.108g/mol
Created on 2018/12/7 22:06

@author: 杜雨威
"""
m = {
    'C': 12.01,
    'H': 1.008,
    'O': 16.00,
    'N': 14.01
}
for cnt in range(int(input())):
    molar = str(input())
    mass = -12.01
    k = 0
    a = 'C'
    for c in molar:
        if c in m:
            if k == 0:
                k = 1
            # print(a, ':', k)
            mass += m[a] * k
            k = 0
            a = c
        else:
            k = k * 10 + int(c)
    if molar[-1] == a:
        mass += m[a]
    else:
        mass += m[a] * k
    mass = "%.3f" % mass
    print(mass)
