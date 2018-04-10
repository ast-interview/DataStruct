# coding: utf-8

class OrderList(object):

    '''
    顺序线性表
    '''

    def __init__(self):
        pass

    def insertIntoByIndex(self, list, index, elem):

        '''
        插入线性表中指定位置：
        1、index插入位置是否合理（1<=index<=len(list)+1）；
        2、list中index-1位置开始及以后的元素依次向后移动一位；
        3、elem插入到list[index-1]
        :param list: 线性表
        :param index: 指定位置
        :param elem: 插入元素
        :return: 插入元素后的线性表
        '''

        list_new = []

        if index < 1 or index > len(list) + 1:
            return list_new

        list_new = list[:index-1]  # list从头到index-1的元素不变
        list_new.append(elem)   # list[index-1]处放置elem
        list_new[len(list_new):len(list_new)] = list[index-1:]  # 原list从index-1处开始放到new list的index处

        return list_new

    def deleteByIndex(self, list, index):

        '''
        删除线性表中指定位置的元素：
        1、index是否合理（1<=index<=len(list)）;
        2、list从index开始，依次向前移动一位。
        :param list: 线性表
        :param index: 指定位置
        :return: 删除后的线性表
        '''

        if index < 1 or index > len(list):
            return []

        list[index-1:] = list[index:]  # list[index]位置及以后的元素依次前移一个位置

        return list



if __name__ == "__main__":
    l = [1, 2, 3, 5, 6]
    order = OrderList()
    print(order.insertIntoByIndex(l, 4, 5))
    print(order.deleteByIndex(l, 6))