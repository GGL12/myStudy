import collections
class Solution:
    def reverseWords(self, s: str) -> str:
        return "".join(reversed(s.split()))

    def fun2(self, s: str) -> str:
        left , right = 0, len(s)-1
        #去掉左右的空格
        while left <= right and s[left] == " ":
            left += 1
        while left <= right and s[right] == " ":
            right -= 1

        #使用双端队列处理 讲单词push到队列的头部
        deque, word = collections.deque(), []
        while left <= right:
            if s[left] == " " and word:
                deque.appendleft("".join(word))
                word = []
            elif s[left] != " ":
                word.append(s[left])
            left += 1
        deque.appendleft("".join(word))
        return "".join(deque)

    def fun3(self, s: str) -> str:
        #倒序遍历 双指针法
        s = s.strip()
        i = j = len(s)-1
        res = []
        while i >= 0:
            #搜索单词空格
            while i>=0 and s[i] != " ":
                i -= 1
            res.append(s[i+1: j+1])
            #跳过空格
            while s[i] == " ":
                i -= 1
            #指针移动
            j = i
        return " ".join(res)
    

