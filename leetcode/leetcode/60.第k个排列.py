class Solution:
    def __init__(self):
        self.res = ""
        self.num = 0
    def getPermutation(self, n, k):
        s = ""
        for i in range(1, n+1):
            s += str(i)
        def backtrack(strs, s, k):
            if len(strs) == n:
                self.num += 1
                if self.num == k:
                    self.res = strs
                return

            for c in s:
                backtrack(strs+c, s.replace(c, ""))
                if self.num == k:
                    return self.res
                else:
                    continue
        backtrack("", s, k)
        return self.res