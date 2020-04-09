class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root):
        #递归
        if not root:
            return None
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left, root.right = right, left

        return root

    def fun2(self, root):
        #用队列进行迭代
        if not root:
            return None
        queue = [root]
        while queue:
            cur = queue.pop(0)
            cur.left, cur.right = cur.right, cur.left
            if cur.left: queue.append(cur.left)
            if cur.right: queue.append(cur.right)
        return root