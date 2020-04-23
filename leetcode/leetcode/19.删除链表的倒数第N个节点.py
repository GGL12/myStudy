class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        '''
        1. 循环找到length
        2. 循环到第n个前面的那个元素
        3. pre.next = pre.next.next 删除节点
        '''

        #设置一个娅节点
        dummy = ListNode(0)
        dummy.next = head
        length = 0
        curNode = head
        #循环找到链表长度
        while curNode != None:
            length += 1
            curNode = curNode.next

        curNode = dummy
        length -= n
        # 循环找到被删除的前一个节点
        while length > 0:
            length -= 1
            curNode = curNode.next
        #删除链表
        curNode.next = curNode.next.next
        return dummy.next

    def fun(self, head, n):
        '''
        双指针法，维护两个指针位置
        '''
        #初始化
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        #first指针先移动n+1
        for i in range(n+1):
            first = first.next
        #first不为Nnoe， first second 一起移动
        #first 移动到底部 second 移动到被删除前一个元素
        while first != None:
            first = first.next
            second = second.next
        #删除元素
        second.next = second.next.next
        return dummy.next

