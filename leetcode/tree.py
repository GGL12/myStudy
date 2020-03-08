class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def pre_order_recusive(root):
    if root == None:
        return None
    print(root.val)
    pre_order_recusive(root.left)
    pre_order_recusive(root.right)

def mid_order_recusive(root):
    if root == None:
        return None
    mid_order_recusive(root.left)
    print(root.val)
    mid_order_recusive(root.right)

def lat_order_recusive(root):
    if root == None:
        return None
    lat_order_recusive(root.left)
    lat_order_recusive(root.right)
    print(root.val)



if __name__ == '__main__':
    #先序遍历 根左右
    #中序遍历 左根右
    #后序遍历 左右根
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t6 = TreeNode(6)
    t7 = TreeNode(7)
    t8 = TreeNode(8)
    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5
    t3.left = t6
    t3.right = t7
    pre_order_recusive(t1)
    mid_order_recusive(t1)
    lat_order_recusive(t1)
