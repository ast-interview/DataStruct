# coding: utf-8
'''
@class: 栈的顺序存储结构
@author: Ivanli
@time:   2017.12.20
'''
class OrderStack(object):

    # 初始化，建立空栈
    def __init__(self, maxsize):
        self.stack = []
        self.top = -1  # 栈顶指针
        self.maxsize = maxsize  # 栈的最大长度

    # 销毁栈
    def destroy(self):
        self.stack = None

    # 清空栈
    def clear(self):
        self.stack = []

    # 栈是否为空
    def IsEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    # 获取栈顶元素
    def getTop(self):
        if self.top != -1:
            return self.stack[self.top]
        else:
            return None

    # 入栈
    def push(self, data):
        if self.top != self.maxsize:
            self.stack.append(data)
            self.top += 1
        else:
            print "Stack is full"
            return None

    # 出栈
    def pop(self):
        if self.top != -1:
            self.top -= 1
            return self.stack.pop()
        else:
            print "Stack is empty"
            return None

    # 统计栈元素的个数
    def getLength(self):
        if self.stack:
            return len(self.stack)
        else:
            print "Stack is not existed"
            return None

