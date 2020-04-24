class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def print_list_from_tail_to_head(self, listNode):
        ret = []
        while listNode:
            ret.insert(0, listNode.val)
            listNode = listNode.next
        return ret