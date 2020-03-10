class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def print_z(self, p_root):
        if not p_root:
            return []
        stack1 = [p_root]
        stack2 = []
        ret = []
        while stack1 or stack2:
            ret_tmp = []
            if stack1:
                tmp_node = stack1.pop()
                ret_tmp.append(tmp_node.val)
                if tmp_node.left:
                    stack2.append(tmp_node.left)
                if tmp_node.right:
                    stack2.append(tmp_node.right)
                ret.append(ret_tmp)
            if stack2:
                tmp_node = stack2.pop()
                ret_tmp.append(tmp_node.val)
                if tmp_node.right:
                    stack1.append(tmp_node.right)
                if tmp_node.left:
                    stack1.append(tmp_node.right)
                ret.append(ret_tmp)
        return ret
