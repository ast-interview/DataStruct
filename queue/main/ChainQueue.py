# coding: utf-8
'''
队列的链式存储结构
@author: Ivanli
@time: 2017/12/26
'''
# coding: utf-8

'''
链表
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
队列的链式存储结构
'''
class ChainQueue(object):

    # 初始化链表
    def __init__(self):
        self.font = None
        self.rear = None

    # 入队列
    def enQueue(self, data):
        # 生成节点
        node = Node(data)

        # 若列表为空，则font,rear指向node
        if self.getLength() == 0:
            self.font = node
            self.rear = node
        else:
            pointer = self.font   # pointer指向font节点
            while pointer._next:
                pointer = pointer._next
            pointer._next = node  # 遍历到最后1个节点，将新节点append上
            self.rear = pointer._next  # rear指向新尾节点

    # 出队列
    def delQueue(self):

        if self.getLength() == 0:  # 队列为空
            print "Queue is empty."
            return None
        del_data = self.font.data
        self.font = self.font._next
        return del_data


    # 获取队列长度
    def getLength(self):
        length = 0
        pointer = self.font
        while pointer:
            length += 1
            pointer = pointer._next
        return length

if __name__ == "__main__":
    ch = ChainQueue()
    for i in range(5):
        ch.enQueue(i)

    for i in range(6):
        print ch.delQueue()