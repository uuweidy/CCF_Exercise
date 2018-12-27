# -*- coding: utf-8 -*-
"""
给出平面上N(N<=1000)个点，问是否可以找到一条*竖线*，使得所有点对称。



思路：如点集存在对称轴，则对称轴为点集x坐标和的平均。然后用set存储每个点(输入点不同),遍历每一个点，通过求得的对称轴，
      计算它的对称点，若不存在则输出“NO”。
Created on 2018/12/27 20:35

@author: 杜雨威
"""
for cnt1 in range(int(input())):
    data = []
    sum_x = 0
    for cnt2 in range(int(input())):
        point = list(map(int, input().strip().split()))
        sum_x += point[0]
        data.append(point)
    ave_x = sum_x / len(data)
    flag = True
    for point in data:
        if [ave_x * 2 - point[0], point[1]] not in data:
            flag = False
            break
    if flag:
        print('YES')
    else:
        print('NO')
