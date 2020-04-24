class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binary_tree_mirror(self, root):
        if root == None:
            return None

        #处理根结点
        root.left, root.right = root.right, root.left
        #处理左右子树
        self.binary_tree_mirror(root.left)
        self.binary_tree_mirror(root.right)