class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def print_from_top_to_bottom(self, root):
        if root == None:
            return []
        support = [root]
        ret = []
        while support:
            tmp_node = support[0]
            ret.append(tmp_node.val)
            if tmp_node.left:
                support.append(tmp_node.left)
            if tmp_node.right:
                support.append(tmp_node.right)

            del support[0]
        return ret