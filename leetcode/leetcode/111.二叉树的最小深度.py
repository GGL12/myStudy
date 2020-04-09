class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root):
        #递归 1
        if not root:
            return 0
        if not root.left:
            return 1 + self.minDepth(root.right)
        if not root.right:
            return 1 + self.minDepth(root.left)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

    def fun2(self, root):
        #递归2
        if not root:
            return 0
        children = [root.left, root.rihgt]
        if not any(children):
            return 1
        min_depth = float("inf")
        for c in children:
            if c:
                min_depth = min(self.minDepth(c), min_depth)
        return min_depth + 1

    def fun3(self, root):
        #DST
        if not root:
            return 0
        else:
            stack, min_depth = [(1, root)], float("inf")
        while stack:
            cur_depth, cur_node = stack.pop()
            if not cur_node.left and not cur_node.right:
                min_depth = min(min_depth, cur_depth)
            if cur_node.left:
                stack.append((cur_depth+1, cur_node.left))
            if cur_node.right:
                stack.append((cur_depth+1, cur_node.right))
        return min_depth

    def fun4(self, root):
        if not root:
            return 0
        else:
            queue = [(1, root)]

        while queue:
            cur_depth, cur_node = queue.pop(0)
            if not cur_node.left and not cur_node.right:
                return  cur_node
            if cur_node.left:
                queue.append((cur_depth+1, cur_node.left))
            if cur_node.right:
                queue.append(cur_depth+1, cur_node.right)

