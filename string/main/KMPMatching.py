# coding: utf-8
'''
@name: KMP匹配算法
@author: Ivanli
@time: 2018/01/04
@desc: 算法流程
1、计算next数组
1.1、next[0]=-1
1.2  next[j]=匹配字符串自身前缀和后缀相等的最长长度
2、匹配
2.1 若主串和匹配串字符相等，则i++,j++，否则主串i不动，匹配串j回溯到next[j]处。
'''

# 初始化next，生成长度和匹配串长度相等的next数组
def initNext(p):
    next = []
    len_p = len(p)
    for i in range(len_p):
        next.append(0)
    return next

# 求next数组
def getNext(p, next):
    next[0] = -1
    i = 0
    j = -1
    while(i < len(p)):
        if j == -1 or p[i] == p[j]:
            i += 1
            j += 1
            if i != len(p):
                next[i] = j
            else:
                break
        else:
            j = next[j]
    return next

def KMP(t, p):
    i = 0
    j = 0
    while (i < len(t) and j < len(p)):
        if j == -1 or t[i] == p[j]:
            i += 1
            j += 1
        else:
            j = next[j]

    if j == len(p):
        return i - j
    else:
        return -1

if __name__ == "__main__":
    t = "ababababca"
    p = "abababca"
    # t = "abcdefgab"
    # p = "abcdex"
    next = initNext(p)
    # print next
    next = getNext(p, next)
    index = KMP(t, p)
    print index