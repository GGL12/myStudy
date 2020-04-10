class Solution:
    def combine(self, n, k):
        #回溯法处理
        res = []
        def backtrack(first, cur=[]):
            if len(cur) == k:
                res.append(cur[:])
            for i in range(first, n+1):
                cur.append(i)
                backtrack(i+1, cur)
                cur.pop()
        backtrack()
        return res