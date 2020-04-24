class Solotion:
    def __init__(self):
        self.input_stack = []
        self.output_stack = []
    def push(self, node):
        #压入栈
        self.input_stack.append(node)
    def pop(self):
        #讲输入栈  反转---》  输出栈
        if self.output_stack == None:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())
        return self.input_stack.pop()



