class Solution:
    def generateMatrix(self, n):
        left, right, top, bottom = 0, n - 1, 0, n - 1
        res = [[0] * n] * n
        num, tar = 1, n * n
        while num <= tar:
            # 从左到右
            for i in range(left, right + 1):
                res[top][i] = num
                num += 1
            top += 1
            # 从上到下
            for i in range(top, bottom + 1):
                res[i][right] = num
                num += 1
            right -= 1
            # 从右到左
            for i in range(right, left - 1, -1):
                res[bottom][i] = num
                num += 1
            bottom -= 1
            # 从下到上
            for i in range(bottom, top - 1, -1):
                res[i][left] = num
                num += 1
            left += 1
        return res
