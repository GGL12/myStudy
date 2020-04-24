# # -*- coding:utf-8 -*-
# # class TreeNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None
# class Solution:
#     def Serialize(self, root):
#         # write code here
#         ret = []
#
#         def pre_order(root):
#             if not root:
#                 ret.append("#")
#                 return
#             ret.append(str(root.val))
#             pre_order(root.left)
#             pre_order(root.right)
#
#         pre_order(root)
#         return ' '.join(ret)
#
#     def Deserialize(self, s):
#         # write code here
#         ret = s.split()
#
#         def de_pre_order():
#             if ret == []:
#                 return None
#             root_val = ret[0]
#             del ret[0]
#             if root_val == "#":
#                 return None
#             node = TreeNode(int(root_val))
#
#             left_node = de_pre_order()
#             right_node = de_pre_order()
#
#             node.left = left_node
#             node.right = right_node
#             return node
#
#         p_root = de_pre_order()
#         return p_root

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.flag = -1
    def serialize(self, root):
        if not root:
            return "#"
        s = str(root.val) + ',' + str(self.serialize(root.left)) + ',' + str(self.serialize(root.right))
        return  s
    def de_serialize(self, s):
        self.flag += 1

        serialize_list = s.split(',')
        if self.flag >= len(s):
            return None

        root = None
        cur_val = serialize_list[self.flag]
        if cur_val != "#":
            root = TreeNode(int(cur_val))
            root.left = self.de_serialize(s)
            root.right = self.de_serialize(s)
        return root

