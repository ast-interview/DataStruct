# coding: utf-8
'''
朴素的模式匹配算法
@author: Ivanli
@time: 2017/12/26
'''
class Match(object):

    def __init__(self):
        pass

    def index(self, s, t, pos):

        for i in range(pos, len(s)):
            flag = False
            index = i
            for j in range(len(t)):
                if s[i] == t[j]:
                    flag = True
                    i = i + 1
                else:
                    flag = False
                    i = index
                    break
            if flag == True:
                return index

        if flag == False:
            return 0


if __name__ == "__main__":
    m = Match()
    a = "acdefgoogle"
    b = "google"
    print m.index(a, b, 0)