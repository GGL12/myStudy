class Solution:
    def isMatch(self, s, p):
        #初始化
        s = "0" + s
        p = "0" + p
        n, m = len(s), len(p)

        dp = [[False] * m] * n
        #初始化
        dp[0][0] = True
        for i in range(1, m):
            dp[0][i] = dp[0][i-1] and p[i] == "*"

        for i in range(1, n):
            for j in range(1, m):
                if s[i] == p[j] or p[j] == "?":
                    dp[i][j] = dp[i-1][j-1]
                elif p[j] == "*":
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
        return dp[-1][-1]
