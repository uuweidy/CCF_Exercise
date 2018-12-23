# -*- coding: utf-8 -*-
"""
输入正整数n以及n个文件名，排序后按列优先的方式左对齐输出。假设最长文件名有M字符，则最右列有M字符，其他列都是M+2字符

Created on 2018/12/19 21:48

@author: 杜雨威
"""
max_line = 60
while 1:
    filenames = []
    length = 0
    try:
        cnt = int(input())
        for i in range(cnt):
            filename = str(input())
            if length < len(filename):
                length = len(filename)
            filenames.append(filename)
    except EOFError:
        break
    filenames = sorted(filenames)
    num = (max_line - length) // (length + 2) + 1
    l = (cnt + num - 1) // num
    # print(length, l, num)
    output_list = []
    for i in range(l):
        line = []
        for j in range(num):
            if l * j + i > len(filenames) - 1:
                pass
            else:
                line.append(filenames[l * j + i])
        output_list.append(line)

    print('-' * 60)
    for i in range(l):
        for j in range(len(output_list[i])):
                if j != len(output_list[i]) - 1:
                    print(output_list[i][j] + (length - len(output_list[i][j]) + 2) * ' ', end='')
                else:
                    print(output_list[i][j] + (length - len(output_list[i][j])) * ' ', end='')
        print()

