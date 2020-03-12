class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def tree_depth(self, p_root):
        if not p_root: return 0
        queue = [p_root]
        res = 0
        while queue:
            n = len(queue)
            for _ in range(n):
                cur_node = queue.pop(0)
                if cur_node.left: queue.append(cur_node.left)
                if cur_node.right: queue.append(cur_node.right)
            res += 1
        return res