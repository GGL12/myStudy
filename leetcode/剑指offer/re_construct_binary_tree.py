class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def re_construct_binary_tree(self, pre, tin):
        if not pre or not tin:
            return None
        if len(pre) != len(tin):
            return None
        #取出根节点
        root = pre[0]
        root_node = TreeNode(root)


        pos = tin.index(root)
        tin_left = tin[:pos]
        tin_right = tin[pos + 1:]
        pre_left = pre[1:pos+1]
        pre_right = pre[pos+1:]

        left_node = self.re_construct_binary_tree(pre_left, tin_left)
        right_node = self.re_construct_binary_tree(pre_right, tin_right)

        if left_node:
            root_node.left = left_node
        if right_node:
            root_node.right = right_node

        return root_node

