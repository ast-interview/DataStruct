# coding: utf-8

'''
双向循环链表
@Author Ivanli
@Time   2017.12.19
'''

'''
节点类
'''
class Node(object):

    def __init__(self, data):
        self.data = data
        self._pre = None   # 前驱
        self._next = None  # 后继

    def __repr__(self):
        return str(self.data)

'''
双向循环链表类
'''
class TwoWayCircleChainTable(object):

    # 初始化链表
    def __init__(self):
        self.head = None
        self.rear = None

    # 添加元素到链表尾部
    def append(self, data):

        # 生成节点
        node = Node(data)

        # 若列表为空，则节点赋给head, rear
        if self.head is None:
            self.head = node
            self.rear = node
            self.head._pre = self.rear   # head.pre  -> rear
            self.head._next = self.rear  # head.next -> rear
            self.rear._pre = self.head   # rear.pre  -> head
            self.rear._next = self.head  # rear.next -> head
        else:
            pointer = self.head   # pointer指向rear节点
            while pointer != self.rear:
                pointer = pointer._next  # 遍历到rear节点
            pointer._next = node  # 遍历到最后1个节点，将新节点append上，pointer为倒数第2个节点
            self.rear = pointer._next  # 更新rear到最后1个节点
            self.rear._pre = pointer   # 更新rear.pre -> pointer
            self.rear._next = self.head  # 更新rear.next -> head

    # 插入节点到链表
    def insert(self, index, data):

        if index < 0 or index > self.getLength():
            return None

        # 生成节点
        node = Node(data)

        # 节点插入头部
        if index == 0:
            tmp_head = self.head         # 备份原头节点
            self.head = node
            self.head._pre = self.rear   # 更新head.pre -> rear
            self.head._next = tmp_head   # 更新head.next -> second
            self.rear._next = self.head  # 更新rear.next -> head
        elif index == self.getLength():
            self.append(data)  # 节点插入尾部
        else:
            pointer = self.head
            i = 0
            while i != index-1:  # 移动指针到index-1位置，找到要插入节点的上一个节点
                pointer = pointer._next
                i += 1
            ori_indexNode = pointer._next  # 备份原先位置的节点，pointer为要插入位置的上1个节点
            pointer._next = node  # 新节点顶替原先节点的位置，作为上一个节点的后继
            node._pre = pointer   # 新节点的pre -> 上1个节点
            node._next = ori_indexNode  # 新节点的next -> 原先节点
            ori_indexNode._pre = node  # 原先节点的pre -> 新节点


    # 删除节点
    def delete(self, index):

        if index < 0 or index > self.getLength():
            return None

        # 删除head节点
        if index == 0:
            self.head = self.head._next
            self.head._pre = self.rear   # 更新新的head.pre -> rear
            self.rear._next = self.head  # 更新rear的后继为新的head
        elif index == self.getLength()-1:  # 删除tail节点
            pointer = self.head
            i = 0
            while i != self.getLength()-1:  # 遍历至rear节点的上一个节点
                pre = pointer
                pointer = pointer._next
                i += 1
            self.rear = pre  # 更新rear节点为上一个节点
            self.rear._next = self.head  # 更新新rear节点的后继节点为head
            self.head._pre = self.rear   # 更新head.pre -> 新rear
        else:
            pointer = self.head
            i = 0
            while i != index-1:
                pointer = pointer._next  # 移动指针到index-1位置，要删除节点的上一个节点
                i += 1
            pointer._next = pointer._next._next  # del节点的上一个节点的next -> del节点的下一个节点
            pointer._next._pre = pointer  # del节点的下一个节点的pre -> del节点的上一个节点

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
        '''
        1. 从head一直遍历到rear，统计节点数目
        2. 最后把rear节点也算上
        :return:
        '''
        length = 0
        pointer = self.head
        while pointer != self.rear:  # 遍历至rear
            length += 1
            pointer = pointer._next
        return length + 1  # 还要将rear节点算上


    # 清空链表
    def clear(self):
        self.head = None
        self.rear = None

'''
操作链表类
'''
class OperateChain(object):

    def __init__(self):
        pass

    # 合并循环链表
    def merge(self, CirChain_1, CirChain_2):

        merge_chain = TwoWayCircleChainTable()

        head_1 = CirChain_1.head
        rear_1 = CirChain_1.rear
        head_2 = CirChain_2.head
        rear_2 = CirChain_2.rear
        rear_1._next = head_2
        head_2._pre = rear_1
        rear_2._next = head_1
        head_1._pre = rear_2

        merge_chain.head = head_1
        merge_chain.rear = rear_2
        return merge_chain

