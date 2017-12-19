# coding: utf-8
'''
@Author Ivanli
@Time   2017.12.19
'''
from chain.ChainTable import ChainTable

'''
测试用例
'''
class TestCase(object):

    def __init__(self):
        pass

    def printChain(self, chain):
        for i in range(chain.getLength()):
            try:
                print chain.getItem(i),
            except Exception as e:
                print str(e)
        print

    # 创建链表
    def createChain(self, chain):
        print "---------------- "
        print "## 创建链表 ##"
        for i in range(5):
            chain.append(i)
        TestCase().printChain(chain)
        return chain

    # 插入节点
    def insertNode(self, chain):
        print "---------------- "
        print "## 插入节点操作 ##"
        print "插入head -> 100"
        chain.insert(0, 100)
        TestCase().printChain(chain)
        print "插入rear -> 1000"
        chain.insert(chain.getLength(), 1000)
        TestCase().printChain(chain)
        print "插入位置3 -> 300"
        chain.insert(3, 300)
        TestCase().printChain(chain)
        return chain


    # 删除节点
    def deleteNode(self, chain):
        print "---------------- "
        print "## 删除节点操作 ##"
        print "删除head"
        chain.delete(0)
        TestCase().printChain(chain)
        print "删除rear"
        chain.delete(chain.getLength()-1)
        TestCase().printChain(chain)
        print "删除位置3"
        chain.delete(3)
        TestCase().printChain(chain)
        return chain

    # 查询元素index
    def getNodeIndex(self, chain):
        print "---------------- "
        print "## 查询元素index ##"
        print "查询数据0"
        print chain.getIndex(0)
        print "查询数据4"
        print chain.getIndex(4)
        print "查询数据300"
        print chain.getIndex(300)

    # 更新链表节点data
    def updateNodeData(self, chain):
        print "---------------- "
        print "## 更新链表元素 ##"
        print "更新head为1000"
        chain.update(0, 1000)
        TestCase().printChain(chain)
        print "更新tear为4000"
        chain.update(chain.getLength()-1, 4000)
        TestCase().printChain(chain)
        print "更新位置2为3000"
        chain.update(2, 3000)
        TestCase().printChain(chain)
        return chain

    # 清空链表
    def clearChain(self, chain):
        print "---------------- "
        print "## 清空链表 ##"
        chain.clear()
        TestCase().printChain(chain)
        return chain

    # 合并链表
    def mergeChain(self, merge_method, chain_1, chain_2):
        print "---------------- "
        print "## 合并链表 ##"
        for i in range(5):
            chain_1.append(i)
        for i in range(5, 10):
            chain_2.append(i)
        merge_chain = merge_method(chain_1, chain_2)
        len = merge_chain.getLength()
        print len
        for i in range(len):
            print merge_chain.getItem(i),

if __name__ == "__main__":
    tc = TestCase()
    chain = ChainTable()
    chain = tc.createChain(chain)
    tc.insertNode(chain)