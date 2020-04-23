class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def mergeTwoLists(self, l1, l2):
        '''
        递归处理 list1[0] + merge(list1[1:], list2) list1[0] < list2[0]
                list2[0] + merge(list1, list2[1:]) else
        '''
        if not l1:
            return l2
        elif not l2:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

    def fun2(self, l1, l2):
        '''
        迭代方法做
        '''
        #设置哑节点
        dummyNode = ListNode(0)
        preNode = dummyNode
        #遍历节点,直到某条链表为空
        while l1 and l2:
            if l1.val < l2.val:
                preNode.next = l1
                l1 = l1.next
            else:
                preNode.next = l2
                l2 = l2.next
            preNode = preNode.next
        #连接非空的链表
        preNode.next = l1 if l1 else l2
        return dummyNode.next

