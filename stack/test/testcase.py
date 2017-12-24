# coding: utf-8
'''
@Author Ivanli
@Time   2017.12.20
'''
from stack.main.OrderStack import OrderStack

'''
测试用例
'''
class TestCase(object):

    def __init__(self):
        pass

    # 创建栈
    def test_createStack(self, maxsize):
        print "---------------- "
        print "## 创建栈 ##"
        stack = OrderStack(maxsize)
        print stack
        return stack

    # 销毁栈
    def test_destroyStack(self, stack, maxsize):
        print "---------------- "
        print "## 销毁栈 ##"
        if stack:
            stack = stack.destroy()
        else:
            print "栈不存在，新建栈"
            stack = OrderStack(maxsize)
            print "入栈"
            stack.push(1)
            print "销毁栈"
            stack = stack.destroy()
        print stack
        return stack

    # 清空栈
    def test_clearStack(self, stack):
        print "---------------- "
        print "## 清空栈 ##"
        if stack == []:
            print "栈为空，入栈"
            stack.push(1)
            print "清空栈"
            stack.clear()
        else:
            stack.clear()
        print stack
        return stack

    # 栈是否为空
    def test_stackIsEmpty(self, stack):
        print "---------------- "
        print "## 栈是否为空 ##"
        if stack == None:
            print "Error: 栈不存在！"
        elif stack.isEmpty():
            print "栈为空"
        else:
            print "栈为不空"
        return stack

    # 获取栈顶元素
    def test_getTop(self, stack):
        print "---------------- "
        print "## 获取栈顶元素 ##"
        if stack:
            print stack.getTop()
        elif stack == []:
            print "Error: 空栈"
        else:
            print "Error: 栈不存在"
        return stack

    # 入栈
    def test_push(self, stack, data):
        print "---------------- "
        print "## 入栈 ##"
        if stack:
            stack.push(data)
        else:
            print "Error: 栈不存在"
        return stack


    # 出栈
    def test_pop(self, stack):
        print "---------------- "
        print "## 出栈 ##"
        if stack:
            print stack.pop()
        else:
            print "Error: 栈不存在"
        return stack


    # 统计栈元素的个数
    def test_getLength(self, stack):
        print "---------------- "
        print "## 统计栈元素的个数 ##"
        if stack:
            print "入栈"
            stack.push(1)
            print stack.getLength()
            print "出栈"
            stack.pop()
            print stack.getLength()
        else:
            print "Error: 栈不存在"

if __name__ == "__main__":
    maxsize = 10
    tc = TestCase()
    stack = tc.test_createStack(maxsize)
    # stack = tc.test_stackIsEmpty(stack)
    # for i in range(11):
    #     stack = tc.test_push(stack, i)
    # tc.test_getLength(stack)
    # stack = tc.test_getTop(stack)
    # for i in range(10):
    #     stack = tc.test_pop(stack)
    # tc.test_getLength(stack)
    # tc.test_stackIsEmpty(stack)
    # tc.test_push(stack, 1)
    # stack = tc.test_clearStack(stack)
    # tc.test_stackIsEmpty(stack)
    print stack == None
    stack = tc.test_destroyStack(stack, maxsize)
    print stack == None