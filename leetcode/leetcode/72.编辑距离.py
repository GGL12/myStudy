class Solution:
    def minDistance(self, word1, word2):
        # 递归的方法处理
        len1, len2 = len(word1), len(word2)
        if len1 == 0 or len2 == 0:
            return max(len1, len2)
        if word1[-1] == word2[-1]:
            return self.minDistance(word1[:-1], word2[:-1])
        return 1 + min(
            self.minDistance(word1, word2[:-1]),
            self.minDistance(word1[:-1], word2),
            self.minDistance(word1[:-1], word2[:-1])
        )

    def minDistance2(self, word1, word2):
        len1, len2 = len(word1), len(word2)
        if len1 * len2 == 0:
            return len1 + len2
        # 初始化dp
        dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]
        for i in range(len1 + 1):
            dp[i][0] = i
        for i in range(len2 + 1):
            dp[0][i] = i
        # 开始动态规划
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
        return dp[-1][-1]
