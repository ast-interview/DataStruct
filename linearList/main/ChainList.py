# coding: utf-8

class Node(object):

    '''
    结点
    '''

    def __init__(self, data):
        self.data = data
        self._next = None

class ChainList(object):

    '''
    链式线性表
    '''

    def __init__(self, data):
        '''
        创建链表
        :param data: 链表的第1个元素的值
        :return: 链表的头结点
        '''
        self.head = Node(data)  # 头结点


    def getIndex(self, data):

        '''
        查找data在链表中的位置:
        1、遍历链表的结点，每个结点的数据与data比较，并计数；
        2、若结点的数据等于data，则返回计数;
        3、若遍历完结点，仍没找到data，则返回False
        :param data:  要查找的data
        :return: index位置
        '''

        index = 1
        p_cur = self.head  # p_cur指向头结点

        while p_cur._next:
            if p_cur.data == data:  # 找到data
                return index
            index = index + 1

        return False  # 遍历完链表，仍没找到data

    def getByIndex(self, index):

        '''
        根据index查找data：
        1、index合法（1<=index<=chain.length()）;
        2、遍历链表，并计数，直到计数等于index，返回该结点的data
        :param index: 结点位置
        :return: 结点data
        '''

        if index < 1 or index > self.length():  # index不合法
            return False

        count = 0
        p_cur = self.head  # p_cur指向头结点
        while count < index-1:
            p_cur = p_cur._next
            count = count + 1

        return p_cur.data


    def length(self):
        
        '''
        获取链表的长度:
        1、若为空链表，返回长度为0；
        2、若不仅有头结点，从头结点开始向后遍历链表，p_cur指针依次当前结点，并计数；
        3、直到p_cur._next为空，return计数
        :return: 链表的长度
        '''
        
        length = 0
        p_cur = self.head  # p_cur指向头结点
        
        if p_cur.data is not None:  # 不为空链表
            while p_cur._next:      # 从头结点开始依次向后遍历结点
                p_cur = p_cur._next
                length = length + 1
            length = length + 1

        return length


    def append(self, data):

        '''
        将结点append到链表:
        1、从头结点开始遍历链表，直到链表当前尾部
        2、将尾部结点的_next指向Node(data)
        :param data: 结点数据
        :return:
        '''

        node = Node(data)
        p_cur = self.head  # p_cur指向头结点

        while p_cur._next:  # 从头结点开始遍历链表，直到链表当前尾部
            p_cur = p_cur._next

        p_cur._next = node



    def insertByIndex(self, index, data):
        '''
        插入链表index位置
        1、index合法（1<=index<=chain.length()）;
        2、新建结点Node(data);
        3、index-1的结点的_next指向Node(data),Node(data)._next指向原index-1结点的_next
        :param index: 插入的index位置
        :param data: 结点数据
        :return:
        '''

        if index < 1 or index > self.length():  # index不合法
            return False

        node = Node(data)

        if index == 1:  # 插入到链表头部
            node._next = self.head  # node._next指向原头结点
            self.head = node        # node作为新的self.head

        if index == self.length():  # 插入到链表尾部
            p_cur = self.head  # p_cur指向头结点
            while p_cur._next:
                p_cur = p_cur._next  # 遍历链表，直到尾部
            p_cur._next = node

if __name__ == "__main__":
    chain = ChainList(1)

    for i in range(2, 5):
        chain.append(i)

    length = chain.length()

    for i in range(length):
        print chain.getByIndex(i+1)
    # chain.insertByIndex()