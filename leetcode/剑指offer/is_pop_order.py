class Solution:
    def is_pop_order(self, pushV, popV):
        # 需要1个栈
        # 按照pushv的方式压入栈
        # 弹出的时候是需要循环判断是否需要弹出
        # 判断是否需要弹出的时机，刚刚压入过后就判断
        # 判断需要弹出的情况的条件，压入栈的顶部和弹出栈的顶部的数据相等
        if pushV == [] or len(pushV) != len(popV):
            return None
        stack = []
        index = 0
        for item in pushV:
            stack.append(item)
            while stack and stack[-1] == popV[index]:
                stack.pop()
                index += 1

        if stack == []:
            return True
        else:
            return False
