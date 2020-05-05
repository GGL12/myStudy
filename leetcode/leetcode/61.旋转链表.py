class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head, k):
        if not head: return None
        if not head.next: return head

        # 将链表闭环，并求出长度
        count = 1
        oldTail = head
        while oldTail.next:
            count += 1
            oldTail = oldTail.next
        oldTail.next = head

        # 找到断点，变成链表
        newTail = head
        for i in range(count - k % count - 1):
            newTail = newTail.next
        newHead = newTail.next
        newTail.next = None
        return newHead
