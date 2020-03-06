class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # def find_frist_common_node(self, p_head1, p_head2):
        # p_tmp1 = p_head1
        # p_tmp2 = p_head2
        # while p_tmp1 and p_tmp2:
        #     p_tmp1 = p_tmp1.next
        #     p_tmp2 = p_tmp2.next
        # k = 0
        # if p_tmp1:
        #     #寻找出链表长度之间的差值
        #     while p_tmp1:
        #         p_tmp1 = p_tmp1.next
        #         k += 1
        #     #让长的那个走k步，使得两个同时在相同长度的节点指针
        #     for i in range(k):
        #         p_tmp1 = p_tmp1.next
        # else:
        #     while p_tmp2:
        #         p_tmp2 = p_tmp2.next
        #         k += 1
        #     for i in range(k):
        #         p_tmp2 = p_tmp2.next
        #
        # while p_tmp1 != p_tmp2:
        #     p_tmp1 = p_tmp1.next
        #     p_tmp2 = p_tmp2.next
        # return p_tmp1

    def find_frist_common_node(self, p_head1, p_head2):
        p_tmp1 = p_head1
        p_tmp2 = p_head2
        while p_tmp1 and p_tmp2:
            p_tmp1 = p_tmp1.next
            p_tmp2 = p_tmp2.next

        if p_tmp1:
            common_node = self.find_equal_node(p_tmp1, p_head2, p_head1)
            return common_node
        else:
            common_node = self.find_equal_node(p_tmp2, p_head1, p_head2)
            return common_node


    def find_equal_node(self, long_p, short_head, long_head):

        k = 0
        while long_p:
            k = k + 1
            long_p = long_p.next

        for i in range(k):
            long_head = long_head.next

        while short_head != long_head:
            short_head = short_head.next
            long_head = long_head.next

        return long_head

