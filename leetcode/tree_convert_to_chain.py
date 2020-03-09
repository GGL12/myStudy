class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def convert(self, pRootOfTree):
        if not pRootOfTree:
            return pRootOfTree
        if not pRootOfTree.left and not pRootOfTree.right:
            return pRootOfTree

        #处理左子树
        self.convert(pRootOfTree.left)
        left = pRootOfTree.left
        #连接根与左子树
        if left:
            while left.right:
                left = left.right
            pRootOfTree.left, left.right = left, pRootOfTree

        #处理右子树
        self.convert(pRootOfTree.right)
        rigth = pRootOfTree.right
        if rigth:
            while rigth.left:
                rigth = rigth.left
            pRootOfTree.right, rigth.left = rigth, pRootOfTree

        while pRootOfTree.left:
            pRootOfTree = pRootOfTree.left
        return pRootOfTree