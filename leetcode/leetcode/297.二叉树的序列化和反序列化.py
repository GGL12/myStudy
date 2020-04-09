class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def serialize(self, root):

        def rserialize(root, string):
            #递归 前序遍历
            if not root:
                string += "None,"
            else:
                string += str(root.val) + ","
                string = rserialize(root.left, string)
                string = rserialize(root.right, string)
            return string
    def deserialize(self, data):

        def rdeserialize(data: list):
            #递归
            if data[0] == "None":
                data.pop(0)
                return None

            root = TreeNode(data[0])
            data.pop(0)
            root.left = rdeserialize(data)
            root.right = rdeserialize(data)

            return root

        data = data.split(",")
        root = rdeserialize(data)
        return root
