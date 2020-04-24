class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        '''
        递归处理
        '''
        #结束条件
        if not head or not head.next:
            return head
        #要交换的节点
        firstNode = head
        secondNode = head.next
        #交换处理
        firstNode.next = self.swapPairs(secondNode.next)
        secondNode.next = firstNode
        return secondNode

    def fun2(self, head):
        '''
        迭代处理
        1. 维护好待交换两节点的前驱和后继
        2. 搞清楚待交换两节点的前驱和后继
        '''
        #设置哑结点
        dummyNode = ListNode(0)
        dummyNode.next = head
        #初始化firstNode的前驱
        preNode = dummyNode
        #开始迭代
        while head and head.next: #保证最后有两个节点
            #初始化节点
            firstNode = head
            secondNode = head.next
            #交换节点
            preNode.next = secondNode
            firstNode.next = secondNode.next
            secondNode.next = firstNode
            #更新preNode head节点
            preNode = firstNode
            head = firstNode.next
        return dummyNode.next