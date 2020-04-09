class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root):
        #递归
        if not root:
            return 0
        else:
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)
            return 1 + max(left, right)


    def fun2(self, root):
        #DFS
        stack = []
        if root:
            stack.append((1, root))
        depth = 0
        while stack:
            cur_depth, cur_node = stack.pop()
            if root:
                depth = max(depth, cur_depth)
                stack.append((cur_depth+1, cur_node.left))
                stack.append((cur_depth+1, cur_node.right))
        return depth
    def fun3(self, root):
        #DFS
        stack = []
        if root:
            stack.append((1, root))
        depth = 0
        while stack:
            cur_depth, cur_node = stack.pop()
            if root:
                depth = max(depth, cur_depth)
                stack.append((cur_depth+1, cur_node.left))
                stack.append((cur_depth+1, cur_node.right))
        return depth