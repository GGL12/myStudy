class Solution:
    def numIslands(self, grid):
        #case
        if not grid:
            return 0
        #赋初值
        row = len(grid)
        col = len(grid[0])
        res = 0
        #循环遍历各个节点，并对每个节点BFS相邻节点
        for i in range(row):
            for j in range(col):
                #判断当前节点是否是岛屿
                if grid[i][j] == "1":
                    #结果+1
                    res += 1
                    #当前节点归0
                    grid[i][j] = '0'
                    #开始BSF相邻节点
                    queue = [(i, j)]
                    while queue:
                        r, c = queue.pop(0)
                        #当前节点的相邻节点
                        for x, y in [(r-1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                            # x, y  在范围内，且相邻节点是岛屿
                            if 0 <= x < row and 0 <= y < col and grid[x][y] == "1":
                                #添加到队列
                                queue.append((x, y))
                                #归置0
                                grid[x][y] = '0'
        return res

    def fun2(self, grid):
        '''
        DFS遍历
        '''
        def dfs(grid, x, y, row, col):

            #判断当前节点在grid中，并且当前节点是岛屿
            if 0 <= x < row and 0 <= y < col and grid[x][y] == "1":
                #岛屿值置为2
                grid[x][y] = '2'
                #递归相邻节点
                dfs(grid, x-1, y, row, col)
                dfs(grid, x+1, y, row, col)
                dfs(grid, x, y-1, row, col)
                dfs(grid, x, y+1, row, col)
        #case
        if not grid:
            return 0
        #赋初值
        row = len(grid)
        col = len(grid[0])
        res = 0
        #循环遍历节点
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    res += 1
                    #消除相邻节点的岛屿
                    dfs(grid, i, j, row, col)
        return res


    "2" + "1"