class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def find_kth_to_tail(self, head, k):

        first_point = head
        second_point = head
        for i in range(k):
            if first_point == None:
                return None
            first_point = first_point.next

        while first_point != None:
            first_point = first_point.next
            second_point = second_point.next

        return second_point