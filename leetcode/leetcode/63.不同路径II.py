class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        if obstacleGrid[0][0] == 1:
            return 0
        #初始化值
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        dp = [[0] * col] * row
        dp[0][0] = 1
        #初始化边界
        for i in range(1, row):
            dp[i][0] = int(dp[i-1][0] == 1 and obstacleGrid[i][0] == 0)
        for i in range(1, col):
            dp[0][i] = int(dp[0][i-1] == 1 and obstacleGrid[0][i] == 0)
        #开始动态规划
        for i in range(row):
            for j in range(col):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                else:
                    dp[i][j] = 0
        return dp[-1][-1]

