# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n > 1:
            num = self.Fibonacci(n - 1) + self.Fibonacci(n - 2)
            return num
        if n < 0:
            return None
        # a = 1
        # b = 0
        # for i in range(n - 1):
        #     ret = a +b
        #     b = a
        #     a = ret
        # return ret

if __name__ == "__main__":
    s = Solution()
    print(s.Fibonacci(500))