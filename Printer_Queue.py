# -*- coding: utf-8 -*-
"""
只有一台打印机，打印任务分1~9的优先级，数字越大优先级越高。
打印机取队首的任务j，如果队列里有优先级更高的任务，则把j放到队列尾部，否则进行打印。每个任务需要1分钟打印时间
输入队列中各个任务的优先级以及所关注的任务在队列中的位置，输出该任务的完成时刻。

Created on 2018/12/31 18:33

@author: 杜雨威
"""
from collections import deque

cnt = int(input())
for i in range(cnt):
    n, pos = map(int, input().strip().split())
    line = list(map(int, input().strip().split()))

    dq = deque(line)
    hq = deque(sorted(line,reverse=True))

    while 1:
        if pos == 0 and dq[0] == hq[0]:
            break

        if dq[0] == hq[0]:
            dq.popleft()
            hq.popleft()
            pos -= 1
        else:
            dq.append(dq.popleft())
            if pos != 0:
                pos -= 1
            else:
                pos = len(dq) - 1

    print(n - len(dq) + 1)


