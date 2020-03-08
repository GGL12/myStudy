class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def has_subtree(self, p_root1, p_root2):
        if p_root1 == None or p_root2 == None:
            return None
        if p_root1.val == p_root2.val:
            ret = self.has_equal(p_root1, p_root2)
            if ret:
                return True
        ret = self.has_subtree(p_root1.left, p_root2)
        if ret:
            return True
        ret = self.has_subtree(p_root1.right, p_root2)
        return ret


    def has_equal(self, p_root1, p_root2):
        if p_root1 == None:
            return False
        if p_root2 == None:
            return True
        if p_root1.val == p_root2.val:
            if p_root2.left == None:
                left_equal = True
            else:
                left_equal = self.has_equal(p_root1.left, p_root2.left)
            if p_root2.right == None:
                right_equal = True
            else:
                right_equal = self.has_equal(p_root1.right, p_root2.right)

            return left_equal and right_equal
        return False
