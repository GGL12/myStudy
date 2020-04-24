class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    def get_next(self, p_node):
        if p_node.right:
            tmp_node = p_node
            while tmp_node.left:
                tmp_node = tmp_node.left
            return tmp_node
        else:
            tmp_node = p_node
            while tmp_node.next:
                if tmp_node.next.left == tmp_node:
                    return tmp_node.next
                tmp_node = tmp_node.next
            return None

