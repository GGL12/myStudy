class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        pre = cur = ListNode(0)
        carry = 0
        while l1 or l2:
            #l1 or l2 没有后序值，统一赋值为0
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            #计算当前的值，进位，结点
            value = (x + y + carry) % 10
            carry = (x + y + carry) // 10
            cur.next = ListNode(value)
            #l1 or l2 跟新
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        #如果最后以为是进位，增新增头部结点
        if carry == 1:
            cur.next = ListNode(1)
        return pre.next
