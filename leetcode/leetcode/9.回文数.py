class Solution:
    def isPalidrome(self, x):
        if x < 0: return False

        #初始化
        cur = 0
        num = x
        while num != 0:
            cur = cur * 10 + num % 10
            num //= 10
        return x == cur