# -*- coding: utf-8 -*-
"""
对于一个n元组（a1, a2, ..., an），可以对于每个数求出它和下一个数的差的绝对值，得到一个新的n元组（|a1 - a2|, |a2 - a3|,
..., |an - a1|）。重复这个过程，得到的序列称为Ducci序列，例如：
（8，11,2,7）->（3,9,5,1）->（6,4,2,2）->（2,0,2,4）->（2,2,2,2）->（0,0,0,0）
也有的Ducci序列最终会循环。输入n元组（3<=n<=15），你的任务是判断它最终会变成0还是会循环。输入保证最多1000步就会变成0或
循环

Created on 2018/12/21 21:59

超时！！！！！！！！！！！！！！！！！！！！！！！！！！！！

@author: 杜雨威
"""
import time
a = int(input())
start = time.clock()
for i in range(a):
    length = int(input())
    num = list(map(int, str(input()).strip().split()))
    temp = num[:]
    res = {}
    while 1:
        a = temp[0]
        for j in range(length):
            if j == length - 1:
                temp[j] = abs(temp[j] - a)
            else:
                temp[j] = abs(temp[j + 1] - temp[j])
        # print(temp, res)
        if res.get(tuple(temp)) is not None:
            break
        res.update({tuple(temp[:]): len(res)})

    is_Loop = False
    for a in range(length):
        if temp[a] != 0:
            is_Loop = True
            break

    if is_Loop:
        print('LOOP')
    else:
        print('ZERO')

elapsed = (time.clock() - start)
print("Time used:", elapsed)
