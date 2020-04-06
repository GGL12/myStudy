class Solution:
    def fib(self, n: int) -> int:
        '''
        递归来做
        :param n:
        :return:
        '''
        if n <= 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)
    def fun2(self, n: int) -> int:
        if n <= 1:
            return n
        if n == 2:
            return  1
        res = 0
        a = 1
        b = 1
        for i in range(3, n+1):
            res = a + b
            a = b
            b = res
        return res
    def fun3(self, n: int) -> int:
        '''
        算法：
        使用黄金分割率计算第 N 个斐波那契数。
        '''
        golden_ratio = (1 + 5**0.5) / 2
        return int((golden_ratio ** n + 1)/ 5**0.5)
    def fun4(self, n: int) -> int:
        """
        dp
        """
        if n <= 1:
            return n
        dp = [0] * (n+1)
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-2] + dp[i-1]
        return dp[-1]