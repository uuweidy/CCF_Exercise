# -*- coding: utf-8 -*-
"""
输入若干行代码，要求各列单词的左边界对齐且尽量靠左。单词之间至少要空一格。每个单词不超过80个字符，每行不超过180个字符，
一共最多1000行。

  start:  integer;    // begins here
stop: integer; //  ends here
 s:  string;
c:   char; // temp


Created on 2018/12/20 16:41

@author: 杜雨威
"""
file = []
while 1:
    try:
        code = str(input()).strip().split()
    except EOFError:
        break
    if len(code) == 0:
        break
    file.append(code)
length = []
for i in range(len(file)):
    while len(file[i]) > len(length):
        length.append(0)
    for j in range(len(file[i])):
        if len(file[i][j]) > length[j]:
            length[j] = len(file[i][j])
# print(length)
for i in range(len(file)):
    for j in range(len(file[i])):
        output_line = file[i][j]
        if j != len(file[i]) - 1:
            if len(file[i][j]) <= length[j]:
                output_line += ' ' * (length[j] - len(file[i][j]) + 1)
        print(output_line, end="")
    print()


