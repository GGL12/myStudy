class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        '''
        暴力遍历所有节点
        排序后增添到链表中
        '''
        #初始化
        nodes = []
        head = point = ListNode(0)
        #暴力遍历
        for listNode in lists:
            while listNode:
                nodes.append(listNode.val)
                listNode = listNode.next
        #排序后添加到链表中
        for node in sorted(nodes):
            point.next = ListNode(node.val)
            point = point.next
        return head.next

    def fun2(self, lists):
        '''
        优先队列处理
        '''
        from queue import PriorityQueue
        head = point = ListNode(0)
        priorityQueue = PriorityQueue()
        for listNode in lists:
            if listNode: priorityQueue.put((listNode.val, listNode))
        while not priorityQueue.empty():
            val, node = priorityQueue.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node: priorityQueue.put((node.val, node))
        return head.next

    def fun3(self, lists):
        '''
        分而治之
        '''
        def merge(listNode1, listNode2):
            head = point = ListNode(0)
            while listNode1 and listNode2:
                if listNode1.val < listNode2.val:
                    point.next = listNode1
                    listNode1 = listNode1.next
                else:
                    point.next = listNode2
                    listNode2 = listNode1
                    listNode1.next = point.next.next
                point = point.next
            if not listNode1: point.next = listNode2
            if not listNode2: point.next = listNode1
            return head.next
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = merge(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else lists
