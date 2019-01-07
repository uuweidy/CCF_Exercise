# -*- coding: utf-8 -*-
"""
输入并模拟执行一段程序，输出第一个bug所在的行。每行程序有两种可能：
    数组定义：格式为arr[size]。例如a[10]或b[5]，可用下标分别是0~9和0~4.定义之后所有元素均为未初始化装填。
    赋值语句：格式为arr[index]=value。例如a[0]=3或者a[a[0]]=a[1]
赋值语句中可能出现两种bug：下标Index越界；使用未初始化的变量
程序不超过1000行，每行不超过80个字符且所有常数均为小于2^31的非负整数

Created on 2019/1/2 18:06

这道题的代码可读性极差，没有进行代码的复用而是直接进行了复制粘贴，不建议阅读

@author: 杜雨威
"""
while 1:
    pro = []
    has_bug = False
    temp = str(input())
    if temp == '.':
        break
    else:
        pro.append(temp)
    while 1:
        temp = str(input())
        if temp == '.':
            break
        else:
            pro.append(temp)
    size_map = {}
    num_map = {}
    for i in range(len(pro)):
        a = pro[i].split('=')
        has_bug = False
        if len(a) == 1:     # 定义语句的处理
            name = a[0][0]
            index = a[0][2:-1]
            nameline = []
            indexline = []
            if not index.isalnum():
                while not index.isalnum():
                    nameline.append(name)
                    name = index[0]
                    index = index[2:-1]
                try:
                    index = num_map[name][index]
                    name = nameline.pop()
                except:
                    has_bug = True
                if has_bug:
                    print(i+1)
                    break
                while len(nameline) != 0:
                    try:
                        index = num_map[name][index]
                        name = nameline.pop()
                    except:
                        has_bug = True
                        break
                try:
                    index = num_map[name][index]
                    name = nameline.pop()
                except:
                    has_bug = True
                if has_bug:
                    print(i+1)
                    break
            size_map.update({name: int(index)})
            num_map.update({name: {}})
            # print(size_map)
        else:               # 赋值语句的处理
            left = a[0]     # 赋值对象
            right = a[1]    # 原值对象
            nameline = []
            indexline = []

            l_name = left[0]
            l_index = left[2:-1]
            if not l_index.isalnum():
                while not l_index.isalnum():
                    nameline.append(l_name)
                    l_name = l_index[0]
                    l_index = l_index[2:-1]
                try:
                    l_index = str(num_map[l_name][l_index])
                    l_name = nameline.pop()
                except:
                    has_bug = True
                if has_bug:
                    print(i+1)
                    break
                while len(nameline) != 0:
                    try:
                        l_index = str(num_map[l_name][l_index])
                        l_name = nameline.pop()
                    except:
                        has_bug = True
                        break

            if size_map[l_name] <= int(l_index):
                has_bug =True
                print(i+1)
                break
            if right.isalnum():
                try:
                    num_map[l_name][l_index] = int(right)
                except:
                    has_bug = True
                    print(i + 1)
                    break
            else:
                r_name = right[0]
                r_index = right[2:-1]
                if not r_index.isalnum():
                    while not r_index.isalnum():
                        nameline.append(r_name)
                        r_name = r_index[0]
                        r_index = r_index[2:-1]
                    try:
                        r_index = str(num_map[r_name][r_index])
                        r_name = nameline.pop()
                    except:
                        has_bug = True
                    if has_bug:
                        print(i+1)
                        break
                    while len(nameline) != 0:
                        try:
                            r_index = str(num_map[r_name][r_index])
                            r_name = nameline.pop()
                        except:
                            has_bug = True
                            break


                try:
                    num_map[l_name][l_index] = num_map[r_name][r_index]
                except:
                    has_bug = True
                    print(i+1)
                    break
    if not has_bug:
        print('0')

