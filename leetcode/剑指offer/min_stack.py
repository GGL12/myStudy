class Solution:

    # def __init__(self):
    #     '''
    #         映射栈的最小值情况
    #     '''
    #     self.stack = []
    #     self.min_map_stack = []
    # def push(self, node):
    #     if self.min_map_stack:
    #         if self.min_map_stack[-1] < node:
    #             self.min_map_stack.append(self.min_map_stack[-1])
    #         else:
    #             self.min_map_stack.append(node)
    #     else:
    #         self.min_map_stack.append(node)
    #     self.stack.append(node)
    #
    # def pop(self):
    #     if self.stack == []:
    #         return None
    #     if self.min_map_stack == []:
    #         return None
    #     self.min_map_stack.pop()
    #     return self.stack.pop()
    #
    # def top(self):
    #     if self.stack == []:
    #         return None
    #     return self.stack[-1]
    #
    # def min(self):
    #     if self.min_map_stack:
    #         return self.min_map_stack[-1]
    #     else:
    #         return None

    '''
        第二种：永远在最后一个元素保留当前的最小值
    '''
    def __init__(self):
        self.stack = []
        self.save_min_stack = []

    def push(self, node):
        if self.save_min_stack:
            if self.save_min_stack[-1] > node:
                self.save_min_stack.append(node)
        else:
            self.save_min_stack.append(node)
        self.stack.append(node)

    def pop(self):

        if self.save_min_stack[-1] == self.stack[-1]:
            self.save_min_stack.pop()
        return self.stack.pop()

    def top(self):

        return self.stack[-1]

    def min(self):

        return self.save_min_stack[-1]
        