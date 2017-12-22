# coding: utf-8
'''
@author Ivanli
@time   2017.12.20
'''
from testcase import TestCase

'''
测试套件
'''
class TestSuites(object):

    def __init__(self):
        pass

    def testOrderStack(self):
        print "** test OrderStack **"
        maxsize = 5
        tc = TestCase()
        stack = tc.test_createStack(maxsize)
        stack = tc.test_stackIsEmpty(stack)
        for i in range(maxsize):
            stack = tc.test_push(stack, i)
        tc.test_push(stack, 6)
        for i in range(maxsize):
            stack = tc.test_getTop(stack)
        # tc.test_getTop(stack)
        # stack = tc.test_stackIsEmpty(stack)
        # stack = tc.test_push(stack, 1)
        # tc.test_getLength(stack)
        # stack = tc.test_clearStack(stack)
        # stack = tc.test_destroyStack(stack)


if __name__ == "__main__":
    ts = TestSuites()
    ts.testOrderStack()