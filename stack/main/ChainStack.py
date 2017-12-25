# coding: utf-8
'''
@class: 栈的链式存储结构
@author: Ivanli
@time:   2017.12.25
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

class ChainStack(object):

    # 初始化，建立空栈
    def __init__(self):
        self.top = None

    # 销毁栈
    def destroy(self):
        self.top = None

    # 清空栈
    def clear(self):
        self.top = None

    # 栈是否为空
    def isEmpty(self):
        if self.top == None:
            return True
        else:
            return False

    # 获取栈顶元素
    def getTop(self):
        if self.top != None:
            return self.top.data
        else:
            return None

    # 入栈
    def push(self, data):
        node = Node(data)
        if self.top == None:  # 第1个节点
            self.top = node
        else:
            node._next = self.top  # 将新节点的后继指向当前栈顶
            self.top = node        # 栈顶指向新节点

    # 出栈
    def pop(self):
        if self.top != None:
            top_data = self.getTop()
            if self.top._next == None:  # 栈底
                self.top = None
            else:
                top = self.top              # 当前栈顶
                self.top = self.top._next   # 栈顶指向当前栈顶的下一个节点
                top = None                  # 释放原栈顶
            return top_data
        else:
            print "Stack is empty"
            return None

    # 统计栈元素的个数
    def getLength(self):
        length = 0
        pointer = self.top
        while pointer:
            length += 1
            pointer = pointer._next
        return length

if __name__ == "__main__":
    stack = ChainStack()
    for i in range(5):
        stack.push(i)
        print stack.getTop()
    print stack.getLength()
    print stack.isEmpty()
    for i in range(6):
        print stack.pop()

    print stack.getLength()
#     print stack.isEmpty()
#     print stack.getTop()
#     for i in range(5):
#         print stack.push(i)
#     print stack.getTop()
#     stack.clear()
#     print stack.isEmpty()
#     stack.destroy()
#     print stack.isEmpty()
    print stack.isEmpty()