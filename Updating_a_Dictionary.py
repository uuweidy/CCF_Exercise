# -*- coding: utf-8 -*-
"""
在本题中，字典是若干键值对，其中键为小写字母组成的字符串，值为没有前导0或正号的非负整数（-4,03和+77都是非法的，注意该整
数可以很大）。输入一个旧字典和一个新字典，计算二者的变化。输入的两个字典中键都是唯一的，但是排列顺序任意，具体格式为（
注意字典格式中不含任何空白字符）：
            {key:value,key:value,...,key:value}
输入包含两行，各包含不超过100个字符，即旧字典和新字典。输出格式如下：
    如果至少有一个新增键，打印一个“+”号，然后是所有新增键，按照字典序从小到大排列
    如果至少有一个删除键，打印一个“-”号，然后是所有删除键，按照字典序从小到大排列
    如果至少有一个修改键，打印一个“*”号，然后是所有修改键，按照字典序从小到大排列
    如果没有任何修改，输出No changes

Created on 2019/1/12 9:50

@author: 杜雨威
"""
from collections import defaultdict


def read_dictionary(dictionary):
    dic = str(input())[1:-1].split(',')
    if dic == ['']:
        dictionary = {}
        return
    for temp in dic:
        key, value = temp.split(':')
        value = int(value)
        dictionary[key] = value


for i in range(int(input())):
    no_changes = True
    add = []
    delete = []
    change = []
    old = defaultdict(lambda: -1)
    new = defaultdict(lambda: -1)

    read_dictionary(old)
    read_dictionary(new)
    # print(old)
    # print(new)

    keys = sorted(set(old.keys()) | set(new.keys()))

    for key in keys:
        old_value = old[key]
        new_value = new[key]
        if old_value == -1:
            add.append(key)
            no_changes = False
        elif new_value == -1:
            delete.append(key)
            no_changes = False
        elif new_value != old_value:
            change.append(key)
            no_changes = False
        else:
            pass

    if no_changes:
        print('No changes')
    else:
        if len(add) != 0:
            print('+', end='')
            print(*add, sep=',')
        if len(delete) != 0:
            print('-', end='')
            print(*delete, sep=',')
        if len(change) != 0:
            print('*', end='')
            print(*change, sep=',')
    print()