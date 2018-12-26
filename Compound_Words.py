# -*- coding: utf-8 -*-
"""
给出一个词典，找出所有的复合词（即恰好有两个单词连接成的单词）。输入每行都是一个由小写字母组成的单词。输入已按照字典序
从小到大排序，且不超过120000个单词。输出所有复合词，按照字典序从小到大排列

Created on 2018/12/26 16:55

@author: 杜雨威
"""
dic = {}
while 1:
    try:
        word = str(input())
        if word == '':
            break
        dic.update({word: 0})
    except EOFError:
        break
ans = []

for word in dic.keys():
    for i in range(1, len(word)):
        if word[:i] in dic and word[i:] in dic:
            ans.append(word)
            break
ans.sort()
for i in ans:
    print(i)
