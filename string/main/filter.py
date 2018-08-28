class Filter(object):
    '''
    过滤掉s中t以外的子字符串
    '''
    def __init__(self, s, t):
        self.s = s
        self.t = t
        self.s_len = len(s)
        self.t_len = len(t)
        self.res = ""

    def filter(self):
        '''
        1、将s看做一个个长度t长度的子字符串，分别跟t比较，若不等，则把当前s字符串起始的字符扔进结果里
        2、否则，下标移动t个长度（因为这3个长度里，s的字符串==t），再重复1的操作
        3、若最后s的子字符串到了最后，不够t长度跟t比较了，直接将这个不够长度的子字符串扔到结果里
        :return:
        '''
        i = 0
        while(i<self.s_len):
            if (i+self.t_len-1)<=self.s_len:
                if s[i:i+self.t_len] != t:
                    self.res = self.res + self.s[i]
                    i += 1
                else:
                    i += 3
            else:
                for i in range(i, self.s_len):
                    self.res = self.res + self.s[i]
                break

        return self.res

if __name__ == "__main__":
    s = "bcabcababcab"
    t = "abc"
    expect = "bcabab"
    f = Filter(s, t)
    res = f.filter()
    print(res)

