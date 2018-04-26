# coding: utf-8

class Sort(object):

    def __init__(self, list):
        self.len = len(list)
        self.list = list

    def bubbleAsc(self):

        for i in range(self.len):
            for j in range(self.len-1-i):
                if self.list[j] > self.list[j+1]:
                    tmp = self.list[j]
                    self.list[j] = self.list[j+1]
                    self.list[j+1] = tmp

    def bubbleDesc(self):
        for i in range(self.len):
            for j in range(self.len-1-i):
                if self.list[j] < self.list[j+1]:
                    tmp = self.list[j]
                    self.list[j] = self.list[j+1]
                    self.list[j+1] = tmp

    def selectAsc(self):
        for i in range(self.len):
            index_max = 0  # 最大元素的下标
            max = self.list[index_max]  # 最大元素
            for j in range(0, self.len-i):
                if max < self.list[j]:
                    max = self.list[j]  # 更新最大元素
                    index_max = j  # 更新最大元素下标
            # 将最大元素与无序序列的最后一个元素交换
            tmp = self.list[index_max]
            self.list[index_max] = self.list[j]
            self.list[j] = tmp

    def selectDesc(self):
        for i in range(self.len):
            index_min = 0
            min = self.list[index_min]
            for j in range(0, self.len-i):
                if min > self.list[j]:
                    index_min = j
                    min = self.list[j]

            tmp = self.list[index_min]
            self.list[index_min] = self.list[j]
            self.list[j] = tmp

    def insertAsc(self):
        for i in range(1, self.len):
            cmp_elem = self.list[i]
            for j in range(i-1, -1, -1):
                if cmp_elem < self.list[j]:
                    self.list[j+1] = self.list[j]
                else:
                    break
            if j == 0 and cmp_elem < self.list[j]:
                self.list[0] = cmp_elem
            else:
                self.list[j+1] = cmp_elem

    def insertDesc(self):
        for i in range(1, self.len):
            cmp_elem = self.list[i]
            for j in range(i-1, -1, -1):
                if cmp_elem > self.list[j]:
                    self.list[j+1] = self.list[j]
            if j == 0 and cmp_elem > self.list[j]:
                self.list[0] = cmp_elem
            else:
                self.list[j+1] = cmp_elem



if __name__ == "__main__":
    sq_list = [10, 7, 5, 3, 2, 1, 4, 6, 8, 9]
    sort = Sort(sq_list)
    sort.bubbleAsc()
    print sort.list
    sort.bubbleDesc()
    print sort.list
    sort.selectAsc()
    print sort.list
    sort.selectDesc()
    print sort.list
    sort.insertAsc()
    print sort.list
    sort.insertDesc()
    print sort.list