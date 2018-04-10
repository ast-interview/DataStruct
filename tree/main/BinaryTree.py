# coding: utf-8
'''
@name:   二叉链表
@author: Ivanli
@time:   2018/01/05
'''

class BitNode(object):
    '''
    结点类
    '''

    def __init__(self, data=-1):
        self.data = data     # 结点数据
        self.lchild = None   # 左孩子指针
        self.rchild = None   # 右孩子指针

    def __repr__(self):
        return str(self.data)

class BinaryTree(object):
    '''
    二叉树类
    '''

    # 构造空树
    def __init__(self):
        self.root = BitNode()
        self.myQueue = []

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
                treeNode.rchild = node   # 否则对右孩子赋值
                self.myQueue.append(treeNode.rchild)
                self.myQueue.pop(0)  # 弹出父结点，让当前父节点的左/右结点作为下一次要插入结点的父结点

    # 利用递归实现树的先序遍历
    def preOrderTraverse(self, root):
        if root == None:
            return None
        print root.data,  # 从根结点开始遍历，打印每次递归的“根结点”
        self.preOrderTraverse(root.lchild)
        self.preOrderTraverse(root.rchild)

    # 利用递归实现树的中序遍历
    def inOrderTraverse(self, root):
        if root == None:
            return None
        self.inOrderTraverse(root.lchild)
        print root.data,
        self.inOrderTraverse(root.rchild)

    # 利用递归实现树的后序遍历
    def postOrderTraverse(self, root):
        if root == None:
            return None
        self.postOrderTraverse(root.lchild)
        self.postOrderTraverse(root.rchild)
        print root.data,

    # 利用堆栈实现树的先序遍历
    def preOrderStack(self, root):
        if root == None:
            return None
        my_stack = []
        node = root
        while node or my_stack:
            while node:  # 从根节点开始，一直找它的左子树
                print node.data,
                my_stack.append(node)
                node = node.lchild  # while结束表示当前节点node为空，即前一个节点没有左子树了
            node = my_stack.pop()
            node = node.rchild   # 开始查看它的右子树

    #  利用堆栈实现树的中序遍历
    def inOrderStack(self, root):
        if root == None:
            return None
        my_stack = []
        node = root
        while node or my_stack:
            while node:  # 从根节点开始，一直找它的左子树
                my_stack.append(node)
                node = node.lchild
            node = my_stack.pop()   # while结束表示当前节点node为空，即前一个节点没有左子树了
            print node.data,
            node = node.rchild

    # 利用堆栈实现树的后序遍历
    def postOrderStack(self, root):
        if root == None:
            return None
        my_stack1 = []
        my_stack2 = []
        node = root
        my_stack1.append(node)
        while my_stack1:   # 这个while循环的功能是找出后序遍历的逆序，存在myStack2里面
            node = my_stack1.pop()
            if node.lchild:
                my_stack1.append(node.lchild)
            if node.rchild:
                my_stack1.append(node.rchild)
            my_stack2.append(node)
        while my_stack2:
            print my_stack2.pop().data,

    # 利用队列实现树的层次遍历
    def levelQueue(self, root):
        if root == None:
            return None
        my_queue = []
        node = root
        my_queue.append(node)
        while my_queue:
            node = my_queue.pop(0)
            print node.data,
            if node.lchild != None:
                my_queue.append(node.lchild)
            if node.rchild != None:
                my_queue.append(node.rchild)




if __name__ == "__main__":
    biTree = BinaryTree()
    for data in range(10):
        biTree.add(data)
    # for data in data_list:
    #     biTree.add(data)

    # print "先序遍历"
    # biTree.preOrderTraverse(biTree.root)
    # print
    print "中序遍历"
    biTree.inOrderTraverse(biTree.root)
    # print
    # print "后序遍历"
    # biTree.postOrderTraverse(biTree.root)
    # print
    # print "利用堆栈实现树的先序遍历"
    # biTree.preOrderStack(biTree.root)
    print
    print "用堆栈实现树的中序遍历"
    biTree.inOrderStack(biTree.root)
    print
    print "利用队列实现树的层次遍历"
    biTree.levelQueue(biTree.root)



