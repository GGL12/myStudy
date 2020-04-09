class Solution:
    def climbStairs(self, n: int) -> int:
        #递归解决
        return self._recursion(0, n)
    def _recursion(self, start: int, end: int) -> int:
        if start > end:
            return 0
        if start == end:
            return 1
        return self._recursion(start+1, end) + self._recursion(start+2, end)

    def fun2(self, n: int) ->int:
        #斐波拉契数
        if n <= 2:
            return n
        a = 1
        b = 2
        for i in range(3, n+1):
            res = a + b
            a = b
            b = res
        return res

    def fun3(self, n: int) ->int:
        #动态规划
        if n == 1:
            return 1
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]
