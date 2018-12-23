# -*- coding: utf-8 -*-
"""
有一个5*5的网格，其中恰好有一个格子是空的，其他格子各有一个字母。一共有4种指令：ABLR，分别表示把空格上下左右的相邻字母
移到空格中。输入初始网格和指令序列（以数字0结束），输出指令执行完毕后的网格。如果有非法指令，应输出"This puzzle has no
final configuration."。

例：  T R G S J                                 T R G S J
      X D O K I           执行ARRBBL0           X O K L I
      M   V L N         =============>>         M D V B N
      W P A B E                                 W P   A E
      U Q H C F                                 U Q H C F

Created on 2018/12/10 21:13

@author: 杜雨威
"""
cnt = 0
while 1:
    cnt += 1
    array = []
    is_end = False
    for i in range(5):
        a = list(input())
        if a == ['Z']:
            is_end = True
            break
        elif len(a) != 5:
            a.append(' ')
        array.append(a)
    # for i in array:
    #     print(i)
    if is_end:
        break
    else:
        command = ''
        c = 'A'
        while c[-1] != '0':
            c = str(input())
            command += c.lower()
        # print(command)
        pos = [0, 0]
        for i in range(5):
            for j in range(5):
                if array[i][j] == ' ':
                    pos = [i, j]
                    break

        # print(pos)
        has_ans = True
        for c in command:
            if c == 'a':
                if pos[0] == 0:
                    has_ans = False
                    break
                array[pos[0]][pos[1]] = array[pos[0] - 1][pos[1]]
                array[pos[0] - 1][pos[1]] = ' '
                pos = [pos[0] - 1, pos[1]]
            elif c == 'b':
                if pos[0] == 4:
                    has_ans = False
                    break
                array[pos[0]][pos[1]] = array[pos[0] + 1][pos[1]]
                array[pos[0] + 1][pos[1]] = ' '
                pos = [pos[0] + 1, pos[1]]
            elif c == 'l':
                if pos[1] == 0:
                    has_ans = False
                    break
                array[pos[0]][pos[1]] = array[pos[0]][pos[1] - 1]
                array[pos[0]][pos[1] - 1] = ' '
                pos = [pos[0], pos[1] - 1]
            elif c == 'r':
                if pos[1] == 4:
                    has_ans = False
                    break
                array[pos[0]][pos[1]] = array[pos[0]][pos[1] + 1]
                array[pos[0]][pos[1] + 1] = ' '
                pos = [pos[0], pos[1] + 1]
            else:
                if c != '0':
                    has_ans = False
                break
        if cnt != 1:
            print()
        print('Puzzle #'+str(cnt)+':')
        if has_ans:
            for i in range(5):
                for j in range(5):
                    print(array[i][j], end='')
                    if j != 4:
                        print(end=' ')
                print()
        else:
            print('This puzzle has no final configuration.')
