# -*- coding: utf-8 -*-
"""
uva511
Created on 2019/1/12 11:01
10ms，惊呆了。
自己写的代码可以简化的地方太多，还是看看别人的吧。

后面的部分是在vjudge上唯一找得到的python代码，地址：
https://cn.vjudge.net/status/#un=&OJId=UVA&probNum=511&res=0&language=PYTHON&onlyFollowee=false
@author: 杜雨威
"""

from collections import defaultdict
map = defaultdict(list)
loc = defaultdict(list)
req = []


def is_in(x, y, x1, y1, x2, y2):
    if x2 <= x <= x1 and y2 <= y <= y1:
        return True
    else:
        return False


temp = str(input())
while 1:
    temp = str(input())
    if temp == 'LOCATIONS':
        break
    else:
        map_name, x1, y1, x2, y2 = temp.split(' ')
        x1, y1, x2, y2 = float(x1), float(y1), float(x2), float(y2)
        if x1 < x2:
            x1, x2 = x2, x1
        if y1 < y2:
            y1, y2 = y2, y1
        area = (x1 - x2) * (y1 - y2)
        ratio = round((x1 - x2) / (y1 - y2), 3)
        map[map_name].extend(i for i in [x1, y1, x2, y2, area, ratio])

while 1:
    temp = str(input())
    if temp == 'REQUESTS':
        break
    else:
        city_name, x, y = temp.split(' ')
        x, y = float(x), float(y)
        loc[city_name].append(x)
        loc[city_name].append(y)

while 1:
    temp = str(input())
    if temp == 'END':
        break
    else:
        city_name, level = temp.split(' ')
        req.append({city_name: int(level)})

# print(map)
# print(loc)
# print(req)

for i in req:
    city = list(i.keys())[0]
    l = list(i.values())[0]
    if len(loc[city]) == 0:
        print(city + ' at detail level ' + str(l) + ' unknown location')
    else:
        bucket = defaultdict(list)
        for temp in map.keys():
            if is_in(loc[city][0], loc[city][1], map[temp][0], map[temp][1], map[temp][2], map[temp][3]):
                bucket[map[temp][4]].append(temp)
        if len(bucket) == 0:
            print(city + ' at detail level ' + str(l) + ' no map contains that location')
            continue
        else:
            k = sorted(bucket.keys(), reverse=True)
            if len(bucket) < l:
                print(city + ' at detail level ' + str(l) + ' no map at that detail level; ', end='')
                temp = bucket[k[-1]]
            else:
                print(city + ' at detail level ' + str(l) + ' ', end='')
                temp = bucket[k[l - 1]]
            # print(temp)
            res = ''
            if len(temp) == 1:
                res = temp[0]
            else:
                min_dis = ((map[temp[0]][0] + map[temp[0]][2]) / 2 - loc[city][0]) ** 2\
                          + ((map[temp[0]][1] + map[temp[0]][3]) / 2 - loc[city][1]) ** 2
                min_ind = 0
                for cnt in range(len(temp)):
                    dis = ((map[temp[cnt]][0] + map[temp[cnt]][2]) / 2 - loc[city][0]) ** 2\
                          + ((map[temp[cnt]][1] + map[temp[cnt]][3]) / 2 - loc[city][1]) ** 2
                    if min_dis > dis:
                        min_dis = dis
                        min_ind = cnt
                for cnt in range(len(temp)):
                    dis = ((map[temp[cnt]][0] + map[temp[cnt]][2]) / 2 - loc[city][0]) ** 2 \
                          + ((map[temp[cnt]][1] + map[temp[cnt]][3]) / 2 - loc[city][1]) ** 2
                    if min_dis != dis:
                        temp.pop(cnt)
                if len(temp) == 1:
                    res = temp[0]
                else:
                    min_rat = abs(map[temp[0]][5] - 0.75)
                    min_ind = 0
                    for cnt in range(len(temp)):
                        if min_rat > abs(map[temp[cnt]][5] - 0.75):
                            min_rat = abs(map[temp[cnt]][5] - 0.75)
                            min_ind = cnt
                    for cnt in range(len(temp)):
                        if min_rat != abs(map[temp[cnt]][5] - 0.75):
                            temp.pop(cnt)
                    if len(temp) == 1:
                        res = temp[0]
                    else:
                        min_dis = (map[temp[0]][0] - loc[city][0]) ** 2 + (map[temp[0]][3] - loc[city][1]) ** 2
                        min_ind = 0
                        for cnt in range(len(temp)):
                            dis = (map[temp[cnt]][0] - loc[city][0]) ** 2 + (map[temp[cnt]][3] - loc[city][1]) ** 2
                            if min_dis > dis:
                                min_dis = dis
                                min_ind = cnt
                        for cnt in range(len(temp)):
                            dis = (map[temp[cnt]][0] - loc[city][0]) ** 2 + (map[temp[cnt]][3] - loc[city][1]) ** 2
                            if min_dis != dis:
                                temp.pop(cnt)
                        if len(temp) == 1:
                            res = temp[0]
                        else:
                            min_x = map[temp[0]][2]
                            min_ind = 0
                            for cnt in range(len(temp)):
                                n = map[temp[cnt]][2]
                                if min_x > n:
                                    min_x = n
                                    min_ind = cnt
                            res = temp[min_ind]
            print('using {}'.format(res))




"""
from math import sqrt
from collections import namedtuple


Location = namedtuple('Location', ['x', 'y'])               # 类似于C中的结构体定义


def cal_dist(l1, l2):
    return sqrt((l1.x - l2.x) ** 2 + (l1.y - l2.y) ** 2)


class Map:
    def __init__(self, name, x1, x2, y1, y2):               # 构造函数的重载
        x1, x2, y1, y2 = min(x1, x2), max(x1, x2), max(y1, y2), min(y1, y2)
        self.name = name
        self.x1, self.x2, self.y1, self.y2 = x1, x2, y1, y2
        self.area, self.ratio = (x2 - x1) * (y1 - y2), (y1 - y2)/(x2 - x1)
        self.center = Location((x1 + x2) / 2, (y1 + y2) / 2)

    def __contains__(self, item):                           # 关键字in的重载？
        return (self.x1 <= item.x <= self.x2) and (self.y2 <= item.y <= self.y1)


input()
maps = []
while 1:
    line = str(input())
    if line == 'LOCATIONS':
        break
    else:
        line = line.split()
        maps.append(Map(line[0], *list(map(float, line[1:]))))      # *的作用是将列表转换为多个参数传递进函数中

locations = {}
while 1:
    line = input()
    if line == 'REQUESTS':
        break
    else:
        line = line.split()
        locations[line[0]] = Location(*list(map(float, line[1:])))

while 1:
    line = input()
    if line == 'END':
        break
    line = line.split()
    name, i = line[0], int(line[1])

    if name not in locations:
        print('{} at detail level {} unknown location'.format(name, i))
    else:
        targets = [m for m in maps if locations[name] in m]

        targets.sort(key=lambda it: it.x1)
        targets.sort(key=lambda it: cal_dist(Location(it.x2, it.y2), locations[name]), reverse=True)
        targets.sort(key=lambda it: abs(it.ratio - 0.75))
        targets.sort(key=lambda it: cal_dist(it.center, locations[name]))
        targets.sort(key=lambda it: it.area, reverse=True)
        # 根据题目要求从后往前进行多次排序，让targets中元素的顺序符合要求

        area_list = sorted(set(m.area for m in targets), reverse=True)
        # 排序地图详细等级
        if not targets:
            print('{} at detail level {} no map contains that location'.format(name, i))
        elif i > len(area_list):
            print('{} at detail level {} no map at that detail level; using {}'.format(name, i, targets[-1].name))
        else:
            for t in targets:
                if t.area == area_list[i - 1]:
                    print('{} at detail level {} using {}'.format(name, i, t.name))
                    break
"""
