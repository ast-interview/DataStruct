# coding: utf-8

'''
选择排序法
'''

class SelectSort(object):

    def __init__(self, sq_list):
        self.sq_list = sq_list
        self.len = len(self.sq_list)

    def asc(self):
        '''
        升序
        :return:
        '''
        for i in range(self.len):
            min = i
            for j in range(i+1, self.len):
                if self.sq_list[min] > self.sq_list[j]:
                    min = j
            if min != i:
                tmp = self.sq_list[min]
                self.sq_list[min] = self.sq_list[i]
                self.sq_list[i] = tmp

    def desc(self):
        '''
        降序
        :return:
        '''
        for i in range(self.len):
            max = i
            for j in range(i+1, self.len):
                if self.sq_list[max] < self.sq_list[j]:
                    max = j
            if max != i:
                tmp = self.sq_list[max]
                self.sq_list[max] = self.sq_list[i]
                self.sq_list[i] = tmp

if __name__ == "__main__":
    sq_list = [9, 1, 5, 8, 3, 7, 4, 6, 2]
    se = SelectSort(sq_list)
    se.asc()
    print se.sq_list
    se.desc()
    print se.sq_list