# coding: utf-8
class sort(object):

    def __init__(self, list):
        self.list = list
        self.len = len(list)

    def swap(self, i, j):
        tmp = self.list[i]
        self.list[i] = self.list[j]
        self.list[j] = tmp

    def quickSort(self, left, right):
        print(left, right)
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
        self.swap(i, left)
        self.quickSort(left, i-1)
        self.quickSort(i+1, right)

    def merge(self, a, b):
        a_len = len(a)
        b_len = len(b)
        i = 0
        j = 0
        tmp = []
        while(i < a_len and j < b_len):
            if a[i] <= b[j]:
                tmp.append(a[i])
                i = i + 1
            else:
                tmp.append(b[j])
                j = j + 1

        while (i < a_len):
            tmp.append(a[i])
            i = i + 1

        while (j < b_len):
            tmp.append(b[j])
            j = j + 1


        if i < a_len:
            tmp_len = len(tmp)
            tmp[tmp_len:tmp_len] = a[i:]
        if j < b_len:
            tmp_len = len(tmp)
            tmp[tmp_len:tmp_len] = b[j:]

        return tmp

    def mergeSort(self, list):
        if len(list) <= 1:
            return list
        mid = len(list)//2
        left = self.mergeSort(list[:mid])
        right = self.mergeSort(list[mid:])
        return self.merge(left, right)

    def adjustTop(self, p, length):
        father = self.list[p]
        i = p*2+1
        while(i<=length):
            if i < length and self.list[i] < self.list[i+1]:
                i = i + 1
            if father > self.list[i]:
                break
            self.swap(i, p)
            p = i
            i = i*2+1
        self.list[p] = father

    def heapSort(self):
        for i in range(self.len//2-1, -1, -1):
            self.adjustTop(i, self.len-1)

        for i in range(self.len-1, 0, -1):
            self.swap(0, i)
            self.adjustTop(0, i-1)

    def shellSort(self):
        inc = self.len
        while(inc>0):
            inc = inc//3+1
            for i in range(inc, self.len):
                ins_elem = self.list[i]
                for j in range(i-inc, -1, -inc):
                    if ins_elem < self.list[j]:
                        self.list[j+inc] = self.list[j]
                    else:
                        break

                if j == 0 and ins_elem < self.list[j]:
                    self.list[j] = ins_elem
                else:
                    self.list[j+inc] = ins_elem
            if inc == 1:
                break

    def insertSort(self):
        for i in range(1, self.len):
            ins = self.list[i]
            for j in range(i-1, -1, -1):
                if ins < self.list[j]:
                    self.list[j+1] = self.list[j]
                else:
                    break
            if j==0 and ins < self.list[j]:
                self.list[j] = ins
            else:
                self.list[j+1] = ins

    def selcetSort(self):
        for i in range(self.len):
            min_index = i
            min_elem = self.list[i]
            for j in range(i+1, self.len):
                if min_elem > self.list[j]:
                    min_elem = self.list[j]
                    min_index = j
            if min_index != i:
                self.swap(i, min_index)


    def search(self, elem):
        left = 0
        right = self.len
        while(left<=right):
            mid = (left+right)//2
            if elem < self.list[mid]:
                right = mid-1
            elif elem > self.list[mid]:
                left = mid+1
            else:
                return mid

def getFbi(n):
    if n == 0 or n == 1:
        return n
    else:
        return getFbi(n-1) + getFbi(n-2)

if __name__ == "__main__":
    l = [50, 10, 90, 30, 70, 40, 80, 60, 20]
    s = sort(l)
    # s.bubbleAsc()
    s.selcetSort()
    # s.insertSort()
    # s.shellSort()
    # res = s.mergeSort(s.list)
    # s.quickSort(0, len(l)-1)
    # s.heapSort()
    print(s.list)
    print(s.search(10))
#     l = [1,2,4]
#     b = [5,6,7]
#     l[len(l):len(l)] = b
#     print(l)
#     tmp = []
#     for i in range(10):
#         tmp.append(getFbi(i))
#
#     print(tmp)