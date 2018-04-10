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
        self.p = None  # 父结点
        self.root = None  # 根结点

    def searchBST(self, key, node=None, p=None):
        '''
        递归查找二叉排序树中是否存在key
        :param key: 要查找的key
        :return:
        '''
        if not node:  # 查找不成功
            self.p = p  # self.p指向node的父结点
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
        if not self.searchBST(key, self.root, self.p):  # 查找不成功
            node = BiTNode(key)
            if not self.p:  # 没有根结点，插入node作为新的根结点
                self.root = node
            elif key < self.p.data:  # 插入node为左孩子
                self.p.lchild = node
            else:
                self.p.rchild = node  # 插入node为右孩子
            return True
        else:
            return False  # 树中已有包含key的结点，不再插入

    def deleteBST(self, key):
        '''
        删除二叉排序树中的key
        :param key:
        :return:
        '''
        pass

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