class TreeNode:
    def __init__(self, x):
        self,val = x
        self.left = None
        self.right = None
class Solution:
    def rightSideView(self, root):
        #深度为索引，存放节点的值
        rightDict = dict()
        #赋初值
        maxDepth = -1
        stack = [(root, 0)]
        #循环栈元素
        while stack:
            #弹出栈顶元素
            node, depth = stack.pop()
            #如果节点存在
            if node:
                #维护二叉树的最大深度
                maxDepth = max(maxDepth, depth)
                #如果不存在对应深度的节点才插入数据
                rightDict.setdefault(depth, node.val)
                #依次入栈左右节点
                stack.append((node.left, depth+1))
                stack.append((node.right, depth+1))
        return [rightDict[depth] for depth in range(maxDepth+1)]

    def fun2(self, root):
        '''
        BSF处理,最后一个值为我们要添加的
        '''
        #深度为索引，存放节点的值
        resDict = dict()
        #初始化值
        maxDepth = -1
        queue = [(root, 0)]
        #循环队列元素
        while queue:
            node, depth = queue.pop(0)
            if node:
                #维护二叉树的最大深度
                maxDepth = max(maxDepth, depth)
                #不断更新当前层的值，直到最后一个为我们的结果值
                resDict[depth] = node.val
                queue.append((node.left, depth+1))
                queue.append((node.right, depth+1))
        return [resDict[depth] for depth in range(maxDepth+1)]
    