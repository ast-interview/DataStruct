# class search(object):
#     def __init__(self):
#         pass
#
#
#     def search(self, list, elem):
#         left = 0
#         right = len(list)
#         while(left<=right):
#             mid = (left+right)//2
#             if elem < list[mid]:
#                 right = mid - 1
#             elif elem > list[mid]:
#                 left = mid + 1
#             else:
#                 return mid

class sort(object):

    def __init__(self, list):
        self.list = list
        self.len = len(list)

    def swap(self, i, j):
        tmp = self.list[i]
        self.list[i] = self.list[j]
        self.list[j] = tmp

    def quickSort(self, left, right):

        if left > right:
            return

        i = left
        j = right
        pivot = self.list[left]
        while(i!=j):

            while(i<j and pivot <= self.list[j]):
                j = j - 1

            while(i<j and pivot >= self.list[i]):
                i = i + 1

            if (i<j):
                self.swap(i, j)

        self.swap(left, i)
        self.quickSort(left, i-1)
        self.quickSort(i+1, right)


    def merge(self, a, b):
        len_a = len(a)
        len_b = len(b)
        i = 0
        j = 0
        tmp_list = []
        while(i < len_a and j < len_b):
            if a[i] < b[j]:
                tmp_list.append(a[i])
                i = i + 1
            else:
                tmp_list.append(b[j])
                j = j + 1
        if i < len_a:
            tmp_len = len(tmp_list)
            tmp_list[tmp_len:tmp_len] = a[i:]

        if j < len_b:
            tmp_len = len(tmp_list)
            tmp_list[tmp_len:tmp_len] = b[j:]


    def mergeSort(self, list):
        if len(list) <= 1:
            return list
        mid = len(list)//2
        left = self.mergeSort(list[:mid])
        right = self.mergeSort(list[mid:])
        self.merge(left, right)


    def adjustTop(self, p, length):
        father = self.list[p]
        i = p*2+1
        while(i<=length):
            if i < length and self.list[i] < self.list[i+1]:
                i = i + 1
            if father > self.list[i]:
                break
            self.list[p] = self.list[i]
            p = i
            i = i*2+1

        self.list[p] = father

    def heapSort(self):
        for i in range(self.len//2-1, -1, -1):
            self.adjustTop(i, self.len-1)

        for i in range(self.len-1, 0, -1):
            self.swap(0, i)
            self.adjustTop(0, i-1)

    def insertSort(self):
        for i in range(1, self.len):
            ins = self.list[i]
            for j in range(i-1, -1, -1):
                if ins < self.list[j]:
                    self.list[j+1] = self.list[j]
                else:
                    break
            if j ==0 and ins < self.list[j]:
                self.list[j] = ins
            else:
                self.list[j+1] = ins


    def selectSort(self):
        for i in range(self.len):
            min = self.list[i]
            min_index = i
            for j in range(i, self.len):
                if min > self.list[j]:
                    min = self.list[j]
                    min_index = j
            if min_index != i:
                self.swap(i, min_index)

    def bubbleSort(self):
        for i in range(self.len):
            for j in range(self.len-1-i):
                if self.list[j] > self.list[j+1]:
                    self.swap(j, j+1)

if __name__ == "__main__":
    l = [50, 10, 90, 30, 70, 40, 80, 60, 20]
    s = sort(l)
    s.bubbleSort()
    print(s.list)

