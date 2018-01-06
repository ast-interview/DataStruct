# coding: utf-8
'''
@name:   线索二叉链表
@author: Ivanli
@time:   2018/01/06
'''

'''
结点类
'''
class BitNode(object):

    def __init__(self, data=-1):
        self.data = data     # 结点数据
        self.lchild = None   # 左孩子指针
        self.rchild = None   # 右孩子指针
        self.ltag = 0        # 前驱标志
        self.rtag = 0        # 后继标志

    def __repr__(self):
        return str(self.data)

'''
线索二叉树类
'''
class ThreadBinaryTree(object):
    # 构造空树
    def __init__(self):
        self.root = BitNode()
        self.myQueue = []
        self.pre = self.root

    # 添加结点
    def add(self, data):
        node = BitNode(data)
        if self.root.data == -1:  # 若为空树，则对根节点赋值
            self.root = node
            self.myQueue.append(self.root)
        else:
            treeNode = self.myQueue[0]  # 当前所在的父节点
            if treeNode.lchild == None:  # 若该节点无左孩子，则对左孩子赋值
                treeNode.lchild = node
                self.myQueue.append(treeNode.lchild)
            else:
                treeNode.rchild = node  # 否则对右孩子赋值
                self.myQueue.append(treeNode.rchild)
                self.myQueue.pop(0)  # 弹出父结点

    # 利用中序遍历进行中序线索化
    def inOrderTraverse(self, root):
        if root == None:
            return None
        self.inOrderTraverse(root.lchild)
        if not root.lchild:  # 没有左孩子
            root.ltag = 1    # 前驱线索
            root.lchild = self.pre
        if not self.pre.rchild:  # 没有右孩子
            self.pre.rtag = 1
            self.pre.rchild = root
        self.pre = root
        print root.data,
        self.inOrderTraverse(root.rchild)

if __name__ == "__main__":
    biTree = ThreadBinaryTree()
    for data in range(10):
        biTree.add(data)
    print "中序遍历"
    biTree.inOrderTraverse(biTree.root)