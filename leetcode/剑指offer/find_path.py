import copy
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def find_path(self, root, except_number):
        #处理root节点为空的情况
        if root == []:
            return []
        #结果保存
        ret = []
        #当前保存的节点
        support = [root]
        #保存当前节点的路径值
        support_array  = [[root.val]]
        #广度优先遍历
        while support:
            tmp_node = support[0]
            tmp_array = support_array[0]
            #判断叶子叶子节点
            if tmp_node.left == None and tmp_node.right == None:
                if sum(tmp_array) == except_number:
                    #巧方法，不必讨论将最长的放回在前面
                    ret.insert(0, tmp_array)
            #处理左节点
            if tmp_node.left:
                support.append(tmp_node.left)
                new_tmp_array = copy.copy(tmp_array)
                new_tmp_array.append(tmp_node.left.val)
                support.append(new_tmp_array)
            #处理右节点
            if tmp_node.right:
                support.append(tmp_node.right)
                new_tmp_array = copy.copy(tmp_array)
                new_tmp_array.append(tmp_node.right.val)
                support_array.append(new_tmp_array)
            #删除当前信息，准备下一轮数据跟新
            del support[0]
            del support_array[0]
        return ret