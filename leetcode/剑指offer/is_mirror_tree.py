class TrueNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def is_symmetrical(self, p_root):

        def is_mirror(left, right):
            if not left and not right:
                return True
            elif not left or not right:
                return False
            if left.val != right.val:
                return False
            ret1 = is_mirror(left.left, right.right)
            ret2 = is_mirror(left.right, right.left)
            return ret1 and ret2

        if not p_root:
            return True
        return is_mirror(p_root.left, p_root.right)