class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def reverseKGroup(self, head, k):
        #设置哑变量
        dummyNode = ListNode(0)
        dummyNode.next = head
        #初始化group节点的head的前驱和最后一个尾巴的节点
        preNode = tailNode = dummyNode
        #开始循环
        while True:
            count = k
            #从起始位置更新尾部节点到正确的位置
            while count and tailNode:
                count -= 1
                tailNode = tailNode.next
            #当剩余节点不足k个时，结束。
            if not tailNode: break
            #保存当前group的head节点，翻转后为尾部节点也就是下一个group的preNode tailNode
            headNode = preNode.next
            while preNode.next != tailNode:
                #当前节点提取出来
                curNode = preNode.next
                '''当前节点开始放置到groub的最后一个节点'''
                #当前节点前驱的后继为当前节点的后继
                preNode.next = curNode.next
                #当前节点的后继为尾部节点的后继
                curNode.next = tailNode.next
                #尾巴的后继为当前节点
                tailNode.next = curNode
            #更新preNode tailNode
            preNode = tailNode = headNode
        return dummyNode.next
