# coding: utf-8

class BubbleSort(object):

    def __init__(self, sq_list):
        self.sq_list = sq_list
        self.len = len(self.sq_list)

    def swap(self, i, j):
        temp = self.sq_list[i]
        self.sq_list[i] = self.sq_list[j]
        self.sq_list[j] = temp

    def asc(self):
        '''
        升序 - 相邻比较
        :return:
        '''
        for i in range(self.len):
            for j in range(self.len-i-1):
                if self.sq_list[j] > self.sq_list[j+1]:
                    self.swap(j, j+1)

    def desc(self):
        '''
        降序 - 相邻比较
        :return:
        '''
        for i in range(self.len):
            for j in range(self.len-i-1):
                if self.sq_list[j] < self.sq_list[j+1]:
                    self.swap(j, j+1)

if __name__ == "__main__":
    sq_list = [9, 1, 5, 8, 3, 7, 4, 6, 2]
    bu = BubbleSort(sq_list)
    bu.asc()
    print bu.sq_list
    bu.desc()
    print bu.sq_list