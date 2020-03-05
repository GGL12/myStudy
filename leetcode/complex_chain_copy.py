class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Sulotion:
    # def clone(self, p_head):
    #     if p_head == None:
    #         return None
    #
    #     #往链表中添加每一个当前的节点
    #     p_tmp = p_head
    #     while p_tmp:
    #         node = RandomListNode(p_head.label)
    #         node.next = p_tmp.next
    #         p_tmp.next = node
    #         p_tmp = p_tmp.next.next
    #
    #     #实现新建node的random
    #     p_tmp = p_head
    #     while p_tmp:
    #         if p_tmp.random:
    #             p_tmp.next.random = p_tmp.random.next
    #         p_tmp = p_tmp.next.next
    #
    #     #断开与新增节点的链接
    #     p_tmp = p_head
    #     new_head = p_head.next
    #     p_new_tmp = new_head
    #     while p_tmp:
    #         p_tmp.next = p_tmp.next.next
    #         if p_new_tmp.next:
    #             p_new_tmp.next = p_new_tmp.next.next
    #             p_new_tmp = p_new_tmp.next
    #         p_tmp = p_tmp.next
    #
    #     return new_head
    def clone(self, p_head):

        if p_head == None:
            return p_head

        cur = p_head
        while cur:
            new_node = RandomListNode(cur.label)
            new_node.next = cur.next
            cur.next = new_node
            cur = new_node.next

        cur = p_head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        new_p_head = p_head.next
        cur = p_head
        cur_next = p_head
        if cur_next:
            cur.next = cur_next.next
            cur = cur_next
            cur_next = cur.next

        return new_p_head
