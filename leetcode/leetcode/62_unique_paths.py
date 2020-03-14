class Solution:
    def uniquePaths(self, m, n):
        '''
            转移方程: f(m-1, n-1) = f(m-2, n-1) + f(m-1, n-2)
        '''
        res = [[0] * n for i in range(m)]
        for row in range(m):
            for col in range(n):
                if not row or not col:
                    res[row][col] = 1
                else:
                    res[row][col] = res[row-1][col] + res[row][col-1]
        return res[-1][-1]