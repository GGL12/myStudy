class Solution:
    def minPathSum(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        dp = [[0] * cols for _ in range(rows)]

        for row in range(rows - 1, -1, -1):
            for col in range(cols - 1, -1, -1):
                if row == rows - 1 and col != cols - 1:
                    dp[row][col] = grid[row][col] + dp[row][col + 1]
                elif row != rows - 1 and col == cols - 1:
                    dp[row][col] = grid[row][col] + dp[row + 1][col]
                elif row != rows - 1 and col != cols - 1:
                    dp[row][col] = grid[row][col] + min(dp[row + 1][col], dp[row][col + 1])
                else:
                    dp[row][col] = grid[row][col]
        return dp[0][0]

    def minPathSum(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        dp = [0] * cols

        for row in range(rows - 1, -1, -1):
            for col in range(cols - 1, -1, -1):
                if row == rows - 1 and col != cols - 1:
                    dp[col] = grid[row][col] + dp[col + 1]
                elif row != rows - 1 and col == cols - 1:
                    dp[col] = grid[row][col] + dp[col]
                elif row != rows - 1 and col != cols - 1:
                    dp[col] = grid[row][col] + min(dp[col], dp[col + 1])
                else:
                    dp[col] = grid[row][col]
        return dp[0]
