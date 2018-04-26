# coding: utf-8

'''
插入排序法
思想：
1、从第N个元素开始，第n个元素之前的元素认为是已经排好顺序的了
2、第N个元素与前n个有序元素比较，从后往前比较
3、若第N个元素<前面的元素，则该前面元素后移1位（腾空地）
4、循环往复步骤2，直到第N个元素>前面的元素，第N个元素插入该前面元素的后面1个位置
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
        j = 0
        for i in range(1, self.len):  # 从第2个元素开始比较，因为第1个元素被认为是已排好序的长度为1的序列
            cmp_elem = self.sq_list[i]  # 待插入的元素
            for j in range(i-1, -1, -1):  # 从已排好序的前面元素序列(长度为i-1)依次往前比较
                if cmp_elem < self.sq_list[j]:  # 若小于前面元素，则前面元素往后移1位（腾空地）
                    self.sq_list[j+1] = self.sq_list[j]
                else:
                    break  # 若大于前面元素，则终止循环，不再比较，将元素插入前面元素的后1位
            if j == 0 and cmp_elem < self.sq_list[j]:  # 若比所有前面元素都小，则插入到首位
                self.sq_list[0] = cmp_elem
            else:
                self.sq_list[j+1] = cmp_elem  # 插入前面元素的后1位

    def desc(self):
        '''
        降序
        :return:
        '''
        j = 0
        for i in range(1, self.len):
            cmp_elem = self.sq_list[i]
            for j in range(i-1, -1, -1):
                if cmp_elem > self.sq_list[j]:
                    self.sq_list[j+1] = self.sq_list[j]
                else:
                    break
            if j == 0 and cmp_elem > self.sq_list[j]:
                self.sq_list[0] = cmp_elem
            else:
                self.sq_list[j+1] = cmp_elem

if __name__ == "__main__":
    sq_list = [10, 7, 5, 3, 2, 1, 4, 6, 8, 9]
    insert = InsertSort(sq_list)
    insert.asc()
    print insert.sq_list
    insert.desc()
    print insert.sq_list