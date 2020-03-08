class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def verify_sequence_of_BST(self, sequence):
        if sequence == []:
            return False
        root_num = sequence[-1]
        del sequence[-1]
        index = None
        for i in range(len(sequence)):
            if index == None and sequence[i] > root_num:
                index = i
            if index != None and sequence[i] < root_num:
                return False
        if sequence[:index] == []:
            return True
        else:
            left_node = self.verify_sequence_of_BST(sequence[:index])
        if sequence[index:] == []:
            return True
        else:
            right_node = self.verify_sequence_of_BST(sequence[index:])

        return left_node and right_node