class Solution:
    #def is_balanced(self, root):
    #nlogn
    #     if not root:
    #         return True
    #     if not self.is_balanced(root.left) or not self.is_balanced(root.right):
    #         return False
    #     if abs(self.height(root.right) - self.height(root.left)) > 1:
    #         return False
    #     return True
    # def height(self, node):
    #     if not node:
    #         return 0
    #     return 1 + max(self.height(node.left), self.height(node.right))

    #O(n)
    def __init__(self):
        self.balanced = True
    def height(self, node):
        if not node:
            return 0
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        if abs(left_height - right_height) > 1:
            self.balanced = False
        return 1 + max(left_height, right_height)

    def is_balanced(self, root):
        if not root:
            return True
        self.height(root)
        return self.balanced