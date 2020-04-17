class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def largestValue(self, root):
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            child = []
            maxValue = float("-inf")
            for node in queue:
                if maxValue < node.val:
                    maxValue = node.val
                if node.left: child.append(node.left)
                if node.right: child.append(node.right)
            res.append(maxValue)
            queue = child
        return res