# -*- coding: utf-8 -*-
"""
输入m个长度均为n的DNA序列，求一个DNA序列，到所有序列的总Hamming距离尽量 小。 两个等长字符串的Hamming距离等于字符不同的
位置个数，例如，ACGT和GCGA的 Hamming距离为2（左数第1, 4个字符不同）。 输入整数m和n（4≤m≤50, 4≤n≤1000），以及m个长度
为n的DNA序列（只包含字母 A，C，G，T），输出到m个序列的Hamming距离和最小的DNA序列和对应的距离。 如有多 解，要求为字典序
最小的解。 例如，对于下面5个DNA序列，最优解为TAAGATAC。

TATGATAC
TAAGCTAC
AAAGATCC
TGAGATAC
TAAGATGT



Sample Input
    3
    5 8
    TATGATAC
    TAAGCTAC
    AAAGATCC
    TGAGATAC
    TAAGATGT
    4 10
    ACGTACGTAC
    CCGTACGTAG
    GCGTACGTAT
    TCGTACGTAA
    6 10
    ATGTTACCAT
    AAGTTACGAT
    AACAAAGCAA
    AAGTTACCTT
    AAGTTACCAA
    TACTTACCAA
Sample Output
    TAAGATAC
    7
    ACGTACGTAA
    6
    AAGTTACCAA
    12

Created on 2018/12/11 22:50

@author: 杜雨威
"""

'''
cnt = int(input())
for k in range(cnt):
    m, n = input().split()
    m = int(m)
    n = int(n)
    cons = []
    ham = []
    for i in range(m):
        s = str(input())
        if len(s) == n:
            cons.append(s)
            ham.append(0)

    for i in range(m):
        for j in range(m):
            if i != j:
                for a in range(n):
                    if cons[i][a] != cons[j][a]:
                        ham[i] += 1
    # print(ham)
    min_num = ham[0]
    for i in ham:
        if min_num > i:
            min_num = i
    # print(min_num)
    min_s = []
    for i in range(m):
        if ham[i] == min_num:
            min_s.append(cons[i])
    # print(min_s)
    m = min_s[0]
    for i in min_s:
        if i < m:
            m = i
    print(m)
    print(min_num)
'''

from collections import Counter

for cas in range(int(input())):
    n, m = map(int, input().strip().split())
    s = []
    for i in range(n):
        s.append(list(input()))
    ans = 0
    for j in range(m):
        news = []
        for i in range(n):
            news.append(s[i][j])
        print("news=", news)
        d = sorted(Counter(news).items(), key=lambda x: (-x[1], x[0]))
        print("d=", d)
        print(d[0][0], end='')
        ans += sum([x[1] for x in d if x[0] != d[0][0]])
        print("ans +", sum([x[1] for x in d if x[0] != d[0][0]]))
    print()
    print(ans)

