class Solution:
    def sum_1_n(self, n):
        return self.sum(n)
    def sum(self, n):
        try:
            1 % n
            return n + self(n-1)
        except:
            return 0