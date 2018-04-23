# coding: utf-8

'''
插入排序法
'''

class InsertSort(object):

    def __init__(self, sq_list):
        self.sq_list = sq_list
        self.len = len(self.sq_list)

    def asc(self):
        '''
        升序
        :return:
        '''
        for i in range(self.len):
            tmp_max = self.sq_list[i]
            for j in range(i+1, self.len):
                if tmp_max > self.sq_list[j]:
                    self.sq_list[j-1] = self.sq_list[j]
                else:
                    self.sq_list[j-1] = tmp_max

if __name__ == "__main__":
    sq_list = [9, 1, 5, 8, 3, 7, 4, 6, 2]
    insert = InsertSort(sq_list)
    insert.asc()
    print insert.sq_list
    # insert.desc()
    # print insert.sq_list