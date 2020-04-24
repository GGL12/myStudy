class ListNode:
    def __int__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverse_list(self, p_head):
        # if p_head == None:
        #     return None
        # if p_head.next == None:
        #     return p_head
        #
        # left_pointer = p_head
        # mid_pointer = p_head.next
        # right_pointer = p_head.next.next
        #
        # #第一个节点作为最后一个节点指向None
        # left_pointer.next = None
        # while right_pointer != None:
        #     mid_pointer.next = left_pointer
        #     left_pointer = mid_pointer
        #     mid_pointer = right_pointer
        #     right_pointer = right_pointer.next
        # mid_pointer.next = left_pointer
        #
        # return mid_pointer

        if not p_head or not p_head.next:
            return p_head

        last = None
        while p_head:
            tmp = p_head.next
            p_head.next = last
            last = p_head
            p_head = tmp
        return last



