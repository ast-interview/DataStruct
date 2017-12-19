# coding: utf-8
from CircleChainTable import CircleChainTable

def printChain(irange):
    for i in range(irange):
        try:
            print chain.getItem(i),
        except Exception as e:
            print str(e)
        print

if __name__ == "__main__":
    chain = CircleChainTable()
    for i in range(5):
        chain.append(i)

    printChain(chain.getLength())
    print "插入节点操作"
    chain.insert(0, 100)
    chain.insert(chain.getLength(), 1000)
    chain.insert(3, 300)
    printChain(chain.getLength())
    print "删除节点操作"
    chain.delete(0)
    printChain(chain.getLength())
    chain.delete(chain.getLength()-1)
    printChain(chain.getLength())
    chain.delete(3)
    printChain(chain.getLength())
    print "查询元素index"
    print chain.getIndex(0)
    print chain.getIndex(4)
    print chain.getIndex(300)
    print "更新链表元素"
    chain.update(0, 1000)
    chain.update(chain.getLength()-1, 4000)
    chain.update(2, 3000)
    printChain(chain.getLength())
    print "清空链表"
    chain.clear()
    printChain(chain.getLength())