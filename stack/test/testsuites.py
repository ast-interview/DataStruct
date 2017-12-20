# coding: utf-8
'''
@author Ivanli
@time   2017.12.20
'''
from stack.main.OrderStack import OrderStack
from testcase import TestCase

'''
测试套件
'''
class TestSuites(object):

    def __init__(self):
        pass

    def testOrderStack(self):
        print "** test OrderStack **"
        maxsize = 10
        tc = TestCase()
        stack = OrderStack()
        stack = tc.test_createStack(maxsize)


if __name__ == "__main__":
    ts = TestSuites()
    ts.testChain()