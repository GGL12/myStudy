class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.rigth = None

class Solution:
    def isValidBST(self, root):
        #递归处理
        def helper(node, lower=float("-inf"), upper=float("inf")):
            #保留父结点
            if not node:
                return True
            val = node.val
            if val <= lower or val >= upper:
                return False
            if not helper(node.left, lower, val):
                return False
            if not helper(node.right, val, upper):
                return False
            return True
        return helper(root)

    def fun2(self, root):
        #迭代 深度优先
        if not root:
            return True
        queue = [(root, float("-inf"), float("inf"))]
        while queue:
            cur, lower, upper = queue.pop(0)
            val = cur.val
            if val <= lower or val >= upper:
                return False
            if cur.left: queue.append((cur.left, lower, val))
            if cur.right: queue.append((cur.right, val, upper))

        return True

    def fun3(self, root):
        stack, inorder = [], float("-inf")
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right
        return True

    def __init__(self):
        self.preValue = None
    def fun4(self, root):
        #中序递归
        if not root:
            return True
        if self.fun4(root.left):
            if self.preValue != None and self.preValue >= root.val:
                return False
            self.preValue = root.val
            return self.isValidBST(root.right)
        return False
