# coding: utf-8
class ShellSort(object):
    '''
    希尔排序
    1、设置步长
    2、将插入排序的1个步长设置为上面的步长
    3、缩减步长，直到步长为1
    '''
    def __init__(self, list):
        self.list = list
        self.len = len(self.list)

    def sortAsc(self):
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
                if j==0 and ins_elem < self.list[j]:
                    self.list[j] = ins_elem
                else:
                    self.list[j+inc] = ins_elem
            if inc == 1:
                break


    def sortDesc(self):
        pass

if __name__ == "__main__":
    list = [50, 10, 90, 30, 70, 40, 80, 60, 20]
    list = [10, 7, 5, 3, 2, 1, 4, 6, 8, 9]

    sort = ShellSort(list)
    sort.sortAsc()
    print(sort.list)