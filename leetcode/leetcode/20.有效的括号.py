class Solution:
    def isValid(self, s):
        #初始化
        stack = []
        table = {"}": "{", ")": "(", "]": "["}
        #遍历字符串
        for char in s:
            if char in table:
                if not stack or table[char] != stack.pop():
                    return False
            else:
                stack.append(char)
        return not stack