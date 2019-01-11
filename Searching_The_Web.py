# -*- coding: utf-8 -*-
"""
输入n篇文章和m个请求（n<100,m<=50000），每个请求都是以下4种格式之一
A：查找包含关键字A的文章
A AND B
A OR B
NOT A
处理询问时，需要对于每篇文章输出证据。前三种询问输出所有至少包含一个关键字的行，第四种询问输出整篇文章。关键字只有小写
字母组成，查找时忽略大小写。每行不超过80个字符，一共不超过1500行。

Created on 2019/1/8 20:50

@author: 杜雨威
"""
import sys
import string
from collections import namedtuple, defaultdict

Article = namedtuple('Article', ['raw'])
# 生成一个元字典（类似于元组），本身名字为Article，其中有一个域，名字为raw。raw中保存每一行的内容，顺序即为输入的顺序
table = defaultdict(lambda: ' ')
table.update({ord(ch): ch for ch in string.ascii_letters})          # ord(ch)将返回ch对应的ascii码
# table中保存ascii字符和对应的数字
bucket = defaultdict(lambda: defaultdict(list))                     # 生成一个形如{0: {0: []}}的字典?
# bucket的保存形式为 bucket[word][art_id][line_index1, line_index2, ...]


def read_article(art_id):
    art = Article([])
    for line_index, line in enumerate(sys.stdin):                   # enumerate返回（下标，内容），参数可以指定下标起始位置
        if line == '*' * 10 + '\n':                                 # 一篇文章的结尾
            break
        art.raw.append(line)
        for word in line.translate(table).lower().split():          # translate函数将line中的字符按照table转换
            if line_index not in bucket[word][art_id]:
                bucket[word][art_id].append(line_index)
                # 对每一行中的每一个词，当这一行的这个词不在bucket中时，行数加入bucket
    return art


db = [read_article(i) for i in range(int(input()))]                 # 读取所有的文章

for i in range(int(input())):
    q = input().lower().split()                                     # 将输入的命令转化为小写
    output = []                                                     # 保存该命令对应的输出内容
    if len(q) == 1:                                                 # A
        word = q[0]                                                 # 要搜索的关键词
        correspond_bucket = bucket[word]                            # 所有含有该关键词的文章以及对应的行号
        for art_id in correspond_bucket:
            output.append(''.join(db[art_id].raw[i]
                                  for i in correspond_bucket[art_id]))
            # 对于含有关键词的所有文章，将所有的行加入output中

    elif len(q) == 2:                                               # NOT A
        word = q[1]                                                 # 要搜索的关键词
        correspond_bucket = bucket[word]                            # 所有含有该关键词的文章以及对应的行号
        for art_id in range(len(db)):
            if art_id not in correspond_bucket:
                output.append(''.join(line for line in db[art_id].raw))
                # 对于所有的文章，当包含关键词的文章不在其中的时候，把整篇文章加入output中

    else:                                                           # A AND B 或者 A OR B
        w1, w2 = q[0], q[2]                                         # 要搜索的关键词
        cb1, cb2 = bucket[w1], bucket[w2]                           # 分别是包含两个关键词的文章中对应的行号
        set_manipulate = '&' if q[1] == 'and' else '|'              # 当命令为and时，变量为‘&’；否则为‘|’
        art_ids = sorted(eval('set(cb1.keys()) {} set(cb2.keys())'.format(set_manipulate)))
        # eval执行并返回一个字符串表达式，这里会返回（同时或者包含其中一个）包含两个关键词的文章编号
        for art_id in art_ids:
            output.append(''.join(db[art_id].raw[i]
                                  for i in range(len(db[art_id].raw))
                                  if i in cb1.get(art_id, []) or i in cb2.get(art_id, [])))
            # 对于包含关键词的文章的行号，假如在含有两个关键词的行号中，则把行号对应的行加入output中

    if output:
        print(*output, sep='-' * 10 + '\n', end='=' * 10 + '\n')
    else:
        print('Sorry, I found nothing.\n', end='=' * 10 + '\n')
    # sep参数会在输出的字符串之间加入参数

"""
def find(temp, keyword):
    pos = temp.find(keyword)
    if pos == -1:
        return -1
    if len(temp) == pos + len(keyword):
        return 1
    else:
        if pos == 0:
            if temp[pos+len(keyword)] == ' ':
                return 1
            else:
                return -1
        else:
            if temp[pos-1] == ' ':
                return 1
            else:
                return -1


article = []
num = int(input())
for cnt1 in range(num):
    content = []
    while 1:
        string = str(input())
        if string == '**********':  # 应该可以优化
            break
        content.append(string)
    article.append(content)
op_num = int(input())
option = []
for cnt1 in range(op_num):
    option.append(str(input()).strip().split())

for op in option:
    has_ans = False
    output = False
    keyword = []
    kind = 0
    if len(op) == 1:                # 此时命令形式为A
        keyword.append(op[0])
        kind = 1
    elif len(op) == 2:              # 此时命令形式为NOT A
        keyword.append(op[1])
        kind = 2
    elif len(op) == 3:
        keyword.append(op[0])
        keyword.append(op[2])
        if op[1] == 'AND':          # 此时命令形式为 A AND B
            kind = 3
        elif op[1] == 'OR':         # 此时命令形式为 A OR B
            kind = 4

    result = []
    pos = []
    for i in range(len(article)):
        result = []
        has1 = False
        has2 = False
        for line in article[i]:
            temp = line.lower()
            if find(temp, keyword[0]) != -1:
                if kind == 1 or kind == 4:
                    result.append(line)
                elif kind == 2:
                    pos.append(i)
                    break
                elif kind == 3:
                    result.append(line)
                    has1 = True
                    if not has2 and find(temp, keyword[1]) != -1:
                        has2 = True
            else:
                if kind == 3:
                    if find(temp, keyword[1]) != -1:
                        result.append(line)
                        has2 = True
                elif kind == 4:
                    if find(temp, keyword[1]) != -1:
                        result.append(line)

        if kind != 2:
            if kind == 3 and not (has1 and has2):
                continue
            if len(result) != 0:
                if output:
                    print('----------')
                else:
                    output = True
            for j in result:
                print(j)
                has_ans = True

    if kind == 2:
        for cnt2 in range(num):
            if cnt2 not in pos:
                if not output:
                    output = True
                else:
                    print('----------')

                for content in article[cnt2]:
                    print(content)
                has_ans = True
    if not has_ans:
        print('Sorry, I found nothing.')
    print('==========')
    output = False
"""