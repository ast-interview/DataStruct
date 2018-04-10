# coding: utf-8
'''
@class:  查找
@author: Ivanli
@time:   2018.01.08
'''

class Search(object):

    def __init__(self):
        pass

    def binary_search(self, search_list, search_key):
        '''
            折半查找
        '''
        low = 0
        high = len(search_list)
        while (low <= high):
            mid = (low + high) / 2
            if (search_list[mid] < search_key):  # search_key在mid右
                low = mid + 1
            elif (search_list[mid] > search_key):  # search_key在mid左
                high = mid - 1
            else:
                return mid

        return None

    def interpolation_search(self, search_list, search_key):
        '''
        插值查找
        mid = low + (high - low) * (search_key - search_list[low]) / (search_list[high] - search_list[low])
        '''
        low = 0
        high = len(search_list)
        while (low <= high):
            mid = low + (high - low) * (search_key - search_list[low]) / (search_list[high] - search_list[low])
            if (search_list[mid] < search_key):  # search_key在mid右
                low = mid + 1
            elif (search_list[mid] > search_key):  # search_key在mid左
                high = mid - 1
            else:
                return mid

        return None


def Fbi(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    return Fbi(i-1) + Fbi(i-2)

if __name__ == "__main__":
    # search_list = [0, 1, 16, 24, 35, 47, 59, 62, 73, 88, 99]
    # search_key = 35
    # se = Search()
    # print se.binary_search(search_list, search_key)
    for i in range(10):
        print Fbi(i),


