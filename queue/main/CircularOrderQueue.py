# coding: utf-8
'''
@class: 队列的循环顺序存储结构
@author: Ivanli
@time:   2017.12.26
'''

class CircularOrderQueue(object):

    def __init__(self, maxsize):
        self.front = 0
        self.rear = 0
        self.maxsize = maxsize
        self.queue = []
        for i in range(self.maxsize):
            self.queue.append(None)

    # 求循环队列长度
    def getQueueLength(self):
        return (self.rear + self.maxsize - self.front) % self.maxsize

    # 入队列
    def enQueue(self, data):
        if (self.rear+1) % self.maxsize == self.front:
            print "Queue is full"
            return False
        else:
            self.queue[self.rear] = data
            self.rear = (self.rear+1) % self.maxsize
            return True

    # 出队列
    def delQueue(self):
        if self.front == self.rear:
            print "Queue is empty"
            return None
        else:
            del_data = self.queue[self.front]
            self.front = (self.front+1) % self.maxsize
            return del_data


if __name__ == "__main__":
    cir = CircularOrderQueue(5)
    for i in range(5):
        cir.enQueue(i)
        print "len: " + str(cir.getQueueLength())
    print cir.queue
    for i in range(5):
        cir.delQueue()
        print "len: " + str(cir.getQueueLength())
    print cir.queue
    cir.enQueue(100)
    cir.enQueue(200)
    cir.enQueue(300)
    cir.enQueue(400)
    cir.enQueue(500)
    print cir.queue
    print "len: " + str(cir.getQueueLength())