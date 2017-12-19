# coding: utf-8

'''
@Author Ivanli
@Time   2017.12.18
'''

'''
节点类
'''
class Node(object):

    def __init__(self, data):
        self.data = data
        self._next = None

    def __repr__(self):
        return str(self.data)

'''
单向链表类
'''
class ChainTable(object):

    # 初始化链表
    def __init__(self):
        self.head = None

    # 添加元素到链表尾部
    def append(self, data):
        # 生成节点
        node = Node(data)

        # 若列表为空，则节点赋给head
        if self.head is None:
            self.head = node
        else:
            pointer = self.head   # pointer指向head节点
            while pointer._next:
                pointer = pointer._next
            pointer._next = node  # 遍历到最后1个节点，将新节点append上



    # 插入节点到链表
    def insert(self, index, data):
        if index < 0 or index > self.getLength():
            return None

        # 生成节点
        node = Node(data)

        # 节点插入头部
        if index == 0:
            tmp_head = self.head
            self.head = node
            self.head._next = tmp_head
        elif index == self.getLength():
            self.append(data)  # 节点插入尾部
        else:
            pointer = self.head
            i = 0
            while i != index-1:  # 移动指针到index-1位置
                pointer = pointer._next
                i += 1
            ori_indexNode = pointer._next
            pointer._next = node
            node._next = ori_indexNode


    # 删除节点
    def delete(self, index):

        if index < 0 or index > self.getLength():
            return None

        # 删除head节点
        if index == 0:
            self.head = self.head._next
        elif index == self.getLength()-1:  # 删除tail节点
            pointer = self.head
            i = 0
            while i != self.getLength()-1:
                pre = pointer
                pointer = pointer._next
                i += 1
            pre._next = None
        else:
            pointer = self.head
            i = 0
            while i != index-1:
                pointer = pointer._next  # 移动指针到index-1位置
                i += 1
            pointer._next = pointer._next._next

    # 更新链表
    def update(self, index, data):

        if index < 0 or index > self.getLength():
            return None
        pointer = self.head
        i = 0
        while i != index:
            pointer = pointer._next
            i += 1
        pointer.data = data

    # 根据index查询节点
    def getItem(self, index):

        if index < 0 or index > self.getLength():
            return None

        pointer = self.head
        i = 0
        while i != index:  # 移动指针到index位置
            pointer = pointer._next
            i += 1
        return pointer.data

    # 根据节点数据查询index
    def getIndex(self, data):

        pointer = self.head
        index = 0
        while pointer.data != data:
            pointer = pointer._next
            index += 1
        return index

    # 获取链表长度
    def getLength(self):
        length = 0
        pointer = self.head
        while pointer:
            length += 1
            pointer = pointer._next
        return length


    # 清空链表
    def clear(self):
        self.head = None