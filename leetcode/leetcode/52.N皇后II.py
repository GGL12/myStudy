class Solution:
    def totalNQueens(self, n):
        #初始化主对角线 斜对角线和一行的记录皇后放置情况
        rows = [0] * n
        hills = [0] * (2 * n - 1)
        dales = [0] * (2 * n - 1)
        #当前位置是否可以放置
        def isNotUnderAttack(row, col):
            return not(rows[col] or hills[row - col] or dales[row + col])
        #当前位置放置皇后
        def placeQueen(row, col):
            rows[col] = 1
            hills[row - col] = 1
            dales[row + col] = 1
        #当前位置恢复
        def removeQueen(row, col):
            rows[col] = 0
            hills[row - col] = 0
            dales[row + col] = 0
        #回溯主体函数
        def backtrack(row=0, count=0):
            #对每一列放置一个皇后
            for col in range(n):
                #如果当前位置可以放
                if isNotUnderAttack(row, col):
                    placeQueen(row, col)
                    #放置n个皇后后count+1
                    if row + 1 == n:
                        count += 1
                    else:
                        #递归下去
                        count = backtrack(row+1, count)
                    #回溯
                    removeQueen(row, col)
            return count
        return backtrack()


