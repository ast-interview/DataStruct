# coding: utf-8
'''
@Author Ivanli
@Time   2017.12.19
'''
from chain.main.ChainTable import ChainTable
from chain.main.CircleChainTable import CircleChainTable
from chain.main.CircleChainTable import OperateChain as CircleOper
from chain.main.TwoWayCircleChainTable import OperateChain as TwoWayOper
from chain.main.TwoWayCircleChainTable import TwoWayCircleChainTable
from testcase import TestCase

'''
测试套件
'''
class TestSuites(object):

    def __init__(self):
        pass

    def testChain(self):
        print "** test Chain **"
        tc = TestCase()
        chain = ChainTable()
        chain = tc.createChain(chain)
        chain = tc.insertNode(chain)
        chain = tc.deleteNode(chain)
        tc.getNodeIndex(chain)
        chain = tc.updateNodeData(chain)
        tc.clearChain(chain)

    def testCircleChain(self):
        print "** test CircleChain **"
        tc = TestCase()
        chain_1 = CircleChainTable()
        chain_2 = CircleChainTable()
        chain_1 = tc.createChain(chain_1)
        chain_1 = tc.insertNode(chain_1)
        chain_1 = tc.deleteNode(chain_1)
        tc.getNodeIndex(chain_1)
        chain_1 = tc.updateNodeData(chain_1)
        chain_1 = tc.clearChain(chain_1)
        tc.mergeChain(CircleOper().merge, chain_1, chain_2)

    def testTwoWayCircleChain(self):
        print "** test TwoWayCircleChain **"
        tc = TestCase()
        chain_1 = TwoWayCircleChainTable()
        chain_2 = TwoWayCircleChainTable()
        chain_1 = tc.createChain(chain_1)
        chain_1 = tc.insertNode(chain_1)
        chain_1 = tc.deleteNode(chain_1)
        tc.getNodeIndex(chain_1)
        chain_1 = tc.updateNodeData(chain_1)
        chain_1 = tc.clearChain(chain_1)
        tc.mergeChain(TwoWayOper().merge, chain_1, chain_2)

if __name__ == "__main__":
    ts = TestSuites()
    ts.testChain()
    ts.testCircleChain()
    ts.testTwoWayCircleChain()