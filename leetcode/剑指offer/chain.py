class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def print_chain(node):
    while node:
        print(node.val)
        node = node.next

if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l1.next = l2
    l2.next = l3
    print_chain(l1)