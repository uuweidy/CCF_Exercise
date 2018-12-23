# -*- coding: utf-8 -*-
"""
给出一个由O和X组成的串（长度为1~80），统计得分。每个O的得分为目前连续出现的O的个数，X的得分为0。
例如，OOXXOXXOOO的得分为1+2+0+0+1+0+0+1+2+3
Created on 2018/12/6 22:21

@author: 杜雨威
"""
ans = []
for i in range(int(input())):
    s = str(input())
    o_num = 0
    score = 0
    for c in s:
        if c == 'O':
            o_num = o_num + 1
            score += o_num
        else:
            o_num = 0
    ans.append(score)
print(ans)
