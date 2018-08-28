# coding: utf-8
class QuickSort(object):

    def __init__(self, list):
        self.list = list
        self.len = len(self.list)

    def swap(self, i, j):
        tmp = self.list[i]
        self.list[i] = self.list[j]
        self.list[j] = tmp

    def sortAsc(self, left, right):
        '''
        快速排序：
        1、选取基准数pivot（选第1个元素），让序列中所有比基金数大的放在右边，小的放左边，构造以基准数为分割的左右2个序列
        2、1的方法是，选取第1个元素为pivot，先从右往左，找比pivot小的数，找到后再从左往右找比pivot大的数，交换这2个数。
        3、再次2步骤，直到左右哨兵相遇（相等），说明pivot应该放的位置找到了，将当初选的pivot（第一个元素）和哨兵相遇处的元素互换位置，这样哨兵相遇左边的元素均小于pivot，右边均大于pivot了。
        2、再分别对基准数以左和右的两个序列分别再选取基准数（第1个元素），再构造1的序列，循环反复。
        :param left: 左哨兵
        :param right: 右哨兵
        :return:
        '''
        if left > right:
            return

        pivot = self.list[left]  # 将第1个元素作为pivot
        i = left  # 左哨兵
        j = right  # 右哨兵


        while (i != j):

            while (i < j and self.list[j] >= pivot):
                j = j - 1  # 找pivot右边比它小的元素

            while(i < j and self.list[i] <= pivot):
                i = i + 1   # 找pivot左边比它大的元素

            if(i < j):
                self.swap(i, j)  # 交换pivot左边大于它的元素和pivot右边小于它的元素

        # 左右哨兵相遇，本轮寻找结束，pivot(left位置)和哨兵位置（i位置）的元素交换
        self.swap(left, i)

        self.sortAsc(left, i-1)  # 继续处理左边的
        self.sortAsc(i+1, right)  # 继续处理右边的（i位置刚结束那轮的pivot不用动了）

    def sortDesc(self, left, right):

        if left > right:
            return

        pivot = self.list[left]
        i = left
        j = right

        while(i != j):

            while(i < j and self.list[j]<=pivot):  # 找pivot右边比它大的元素
                j = j - 1

            while(i < j and self.list[i]>=pivot):  # 找pibot左边比它小的元素
                i = i + 1

            if (i < j):
                self.swap(i, j)

        self.swap(left, i)
        self.sortDesc(left, i-1)
        self.sortDesc(i+1, right)



if __name__ == "__main__":
    l = [50, 10, 90, 30, 70, 40, 80, 60, 20]
    s = QuickSort(l)
    # s.sortAsc(0, len(s.list)-1)
    s.sortDesc(0, len(s.list)-1)
    print(s.list)