class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        queue = [root]
        res = []
        while queue:
            cur_val = []
            child = []
            for item in queue:
                cur_val.append(item.val)
                if item.left: child.append(item.left)
                if item.right: child.append(item.right)
            res.append(cur_val)
            queue = child
        return res

    def fun2(self, root):
        if not root:
            return []
        res = []
        def dfs(root, level):
            if len(res) == level:
                res.append([])
            res[level].append(root.val)
            if root.left: dfs(root.left, level+1)
            if root.right: dfs(root.right, level+1)
        dfs(root, 0)
        return res
