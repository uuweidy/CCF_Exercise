# -*- coding: utf-8 -*-
"""
模拟一个图书管理系统。首先输入若干图书的标题和作者（标题各不相同，以END结束），然后是若干指令：BORROW指令表示借书，
RETURN指令表示还书，SHELVE指令表示把所有已归还但未上架的图书排序后依次插入书架并输出图书标题和插入位置（可能是第一本书
或者某本书的后面）。
图书排序的方法是先按作者从小到大排，再按标题从小到大排。在处理第一条指令之前，你应当先将所有图书按照这种方式排序。

Created on 2019/1/1 9:48

@author: 杜雨威
"""
carrier = {}
while 1:
    temp = input().split('by')
    if temp == ['END']:
        break
    book, name = temp[0][1:-2], temp[1][1:]
    carrier.update({book: [name, 1]})       # 书名：[作者名称，状态（在库）]


while 1:
    # print(sorted(carrier.items(), key=lambda x: (x[1][0], x[0])))
    order = input().split(' ', 1)
    target = ''
    if order == ['SHELVE']:
        l = sorted(carrier.items(), key=lambda x: (x[1][0], x[0]))
        pos = -1
        # print(l)
        for i in range(len(l)):
            if carrier.get(l[i][0])[1] == 0:
                if i == 0 or pos == -1:
                    print('Put "' + l[i][0] + '" first')
                else:
                    print('Put "' + l[i][0] + '" after "' + l[pos][0] + '"')
                carrier.update({l[i][0]: [carrier.get(l[i][0])[0], 1]})
                pos = i
            if carrier.get(l[i][0])[1] == 1:
                pos = i
        print('END')
        continue
    elif order == ['END']:
        break
    order, target = order[0], order[1][1:-1]
    # print(order, target)
    if order == 'BORROW':
        carrier.update({target: [carrier.get(target)[0], -1]})
    elif order == 'RETURN':
        carrier.update({target: [carrier.get(target)[0], 0]})

