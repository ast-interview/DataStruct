# coding: utf-8

class BiTNode(object):
    '''
    二叉树的二叉链表结点
    '''
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

class BST(object):

    '''
    二叉排序树（二叉查找树）
    '''

    def __init__(self):
        self.curNode = None  # 当前结点
        self.root = None  # 根结点

    def searchBST(self, key, node=None, curNode=None):
        '''
        递归查找二叉排序树中是否存在key
        :param key: 要查找的key
        :return:
        '''
        if not node:  # 查找不成功
            self.curNode = curNode  # self.curNode指向node的父结点
            return False
        elif key == node.data:  # 查找成功
            return True
        elif key < node.data:  # 继续在左子树查找
            self.searchBST(key, node.lchild, node)
        else:                  # 继续在右子树查找
            self.searchBST(key, node.rchild, node)

    def insertBST(self, key):
        '''
        当二叉排序树种不存在key时，插入key并返回True，否则返回False
        :param key:
        :return:
        '''
        if not self.searchBST(key, self.root, self.curNode):  # 查找不成功
            node = BiTNode(key)
            if not self.curNode:  # 没有根结点，插入node作为新的根结点
                self.root = node
            elif key < self.curNode.data:  # 插入node为左孩子
                self.curNode.lchild = node
            else:
                self.curNode.rchild = node  # 插入node为右孩子
            return True
        else:
            return False  # 树中已有包含key的结点，不再插入

    def deleteBST(self, key, curNode, father):
        '''
        删除二叉排序树中的key
        :param key: 要删除的key
        :param curNode: 当前结点
        :param father: 当前结点的父结点
        :return:
        '''
        father = father

        if curNode is None:  # 不存在key
            return False
        else:
            if curNode.data == key:  # 找到key
                self.deleteKey(curNode, father)
            elif key < curNode.data:
                self.deleteBST(key, curNode.lchild, curNode)
            else:
                self.deleteBST(key, curNode.rchild, curNode)

    def deleteKey(self, curNode, father):
        '''
        从二叉排序树删除结点curNode，并重接它的左右孩子树
        :param curNode: 当前结点
        :param father: 当前结点的父结点
        :return:
        '''

        if curNode.lchild is None:  # 左子树为空，重接它的右子树
            if father.lchild == curNode:  # 当前结点是父结点的左结点
                father.lchild = curNode.rchild
            else:
                father.rchild = curNode.rchild  # 当前结点是父结点的右结点

        elif curNode.rchild is None:  # 右子树为空，重接它的左子树
            if father.lchild == curNode:  # 当前结点是父结点的左结点
                father.lchild = curNode.lchild
            else:
                father.rchild = curNode.lchild  # 当前结点是父结点的右结点

        else:  # 左右子树均不为空

            s = curNode.lchild  # 找左子树中curNode的直接前驱，即找左子树中的最右尽头结点
            p = curNode         # p为s的父结点

            while(s.rchild):
                p = s
                s = s.rchild
            curNode.data = s.data  # 将curNode的data替换为直接前驱的data

            if p != curNode:  # curNode的左孩子有右孩子，即while生效了
                p.rchild = s.lchild  # 把s的左孩子赋给s的父结点的右孩子(因为s为最右结点，所以s是没有右孩子的)，即删掉了s结点（s结点的数据替换到curNode了）
            else:             # curNode的左孩子没有右孩子
                p.lchild = s.lchild  # 把s的左孩子赋给s的父结点的左孩子

            del s

        return True


    def inOrderTraverse(self, root):
        '''
        中序遍历二叉顺序树
        :return:
        '''
        if root == None:  # 树不存在
            return None
        self.inOrderTraverse(root.lchild)
        print root.data,
        self.inOrderTraverse(root.rchild)



if __name__ == "__main__":
    l = [62, 88, 58, 47, 35, 73, 51, 99, 37, 93]
    bst = BST()
    for i in l:
        bst.insertBST(i)

    bst.inOrderTraverse(bst.root)
    print
    bst.deleteBST(35, bst.root, None)
    bst.inOrderTraverse(bst.root)
    print
    bst.deleteBST(62, bst.root, None)
    bst.inOrderTraverse(bst.root)
    print
    bst.deleteBST(93, bst.root, None)
    bst.inOrderTraverse(bst.root)