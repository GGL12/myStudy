# class Solution:
#     # 返回二维列表[[1,2],[4,5]]
#     def Print(self, pRoot):
#         # write code here
#         if not pRoot:
#             return []
#         quene1 = [pRoot]
#         quene2 = []
#         ret = []
#         while quene1 or quene2:
#             tmp_ret = []
#             if quene1:
#                 while quene1:
#                     tmp_node = quene1[0]
#                     tmp_ret.append(tmp_node.val)
#                     del quene1[0]
#                     if tmp_node.left:
#                         quene2.append(tmp_node.left)
#                     if tmp_node.right:
#                         quene2.append(tmp_node.right)
#                 ret.append(tmp_ret)
#             if quene2:
#                 while quene2:
#                     tmp_node = quene2[0]
#                     tmp_ret.append(tmp_node.val)
#                     del quene2[0]
#                     if tmp_node.left:
#                         quene1.append(tmp_node.left)
#                     if tmp_node.right:
#                         quene1.append(tmp_node.right)
#                 ret.append(tmp_ret)
#         return ret

class Solution:
    def line_print(self, p_root):

        if not p_root:
            return []
        self.ret = []
        quene1 = [p_root]
        quene2 = []
        while quene1 or quene2:
            if quene1:
                self._exec_and_append(quene1, quene2)
            if quene2:
                self._exec_and_append(quene2, quene1)
        return self.ret

    def _exec_and_append(self, exec_quene, append_quene):
        tmp_ret = []
        while exec_quene:
            tmp_node = exec_quene[0]
            del exec_quene[0]
            tmp_ret.append(tmp_node.val)
            if tmp_node.left:
                append_quene.append(tmp_node.left)
            if tmp_node.right:
                append_quene.append(tmp_node.right)
        self.ret.append(tmp_ret)