# coding: utf-8
'''
堆是具有以下性质的完全二叉树：
1、每个结点的值都大于或等于其左右孩子结点的值，称为大顶堆；
大顶堆：arr[i] >= arr[2i+1] && arr[i] >= arr[2i+2]
2、或者每个结点的值都小于或等于其左右孩子结点的值，称为小顶堆。
小顶堆：arr[i] <= arr[2i+1] && arr[i] <= arr[2i+2]

堆排序：
1、将待排序的序列构造成一个大（小）顶堆，此时整个序列的最大（小）值就是堆顶的根结点
2、将它与末尾元素进行交换
3、将剩余n-1个序列重新构造堆，反复2，3
'''
class HeapSort(object):

    def __init__(self, list):
        self.len = len(list)
        self.list = list

    def heapAdjustBig(self, p, length):
        '''
        将list[p:m]调整为一个大顶堆
        :param p: 父结点下
        :param length: 当前待排列序列长度
        :return: 大顶堆
        '''

        tmp_father = self.list[p]  # 备份当前父结点
        i = p*2+1
        while(i<=length):
            # print("i: " + str(i))
            if i < length and self.list[i] < self.list[i+1]:  # 右孩子结点大于左孩子结点
                i = i + 1  # i为值最大的结点的下标
            if tmp_father > self.list[i]:  # 若父亲结点比左右孩子均大，则不交换
                break
            self.list[p] = self.list[i]  # 最大元素替换到父结点上
            p = i  # 记录替换前的最大元素的下标
            i = i*2+1  # 当前结点的左孩子结点
        self.list[p] = tmp_father  # 将父结点的元素置在之前最大元素的位置上

    def sortAsc(self):
        '''
        堆排序 -- 升序
        :return:
        '''
        for i in range(self.len//2-1, -1, -1):  # 将self.list构造成大顶堆
            self.heapAdjustBig(i, self.len-1)

        for i in range(self.len-1, 0, -1):
            self.swap(0, i)  # 将堆顶记录和未经排序的子序列的最后一个元素进行交换
            self.heapAdjustBig(0, i-1)  # 将前i-1个元素重新构造大顶堆


    def swap(self, i, j):
        '''
        交换元素
        :param i:
        :param j:
        :return:
        '''
        tmp = self.list[i]
        self.list[i] = self.list[j]
        self.list[j] = tmp

    def heapAdjustLow(self, p, length):
        '''
        将self.list[p:length]调整为小顶堆
        :param p: 父结点下标
        :param length: 当前待排列序列长度
        :return: 小顶堆
        '''
        tmp_father = self.list[p]
        i = p*2+1
        while(i<=length):
            if i < length and self.list[i] > self.list[i+1]:
                i = i + 1
            if tmp_father < self.list[i]:
                break
            self.list[p] = self.list[i]
            p = i
            i = i*2+1
        self.list[p] = tmp_father

    def sortDesc(self):
        '''
        堆排序 -- 降序
        :return:
        '''

        for i in range(self.len//2+1, -1, -1):
            self.heapAdjustLow(i, self.len-1)  # 构造小顶堆

        for i in range(self.len-1, 0, -1):
            self.swap(0, i)  # 将堆顶元素和未经排序的子序列的最后一个元素进行交换
            self.heapAdjustLow(0, i-1)  # 将前i-1个元素重新构造小顶堆


if __name__ == "__main__":
    list = [50, 10, 90, 30, 70, 40, 80, 60, 20]
    hs = HeapSort(list)
    hs.sortAsc()
    print hs.list
    hs.sortDesc()
    print hs.list
