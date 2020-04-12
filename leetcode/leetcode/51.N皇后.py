class Solution:
    def solveNQueens(self, n):
        if n < 1:
            return []
        self.result = []
        self.cols = set()
        self.pie = set()
        self.na = set()

        self.DFS(n, 0, [])
        return self._generate_result(n)

    def DFS(self, n, row, cur_state):
        if row >= n:
            self.result.append(cur_state)
            return
        for col in range(n):
            if col in self.cols or row+col in self.pie or row-col in self.na:
                continue
            self.cols.add(col)
            self.pie.add(row+col)
            self.na.add(row-col)
            self.cols.remove(col)
            self.pie.remove(row+col)
            self.na.remove(row-col)

    def _generate_result(self, n):
        board = []
        for res in self.result:
            for i in res:
                board.append("." * i + "Q" + "." * (n-i-1))
        return [board[i: i+n] for i in range(0, len(board), n)]


    def fun2(self, n):
        def DFS(queues, xy_dif, xy_sum):
            row = len(queues)
            if row == n:
                result.append(queues)
                return None
            for col in range(n):
                if col not in queues and row-col not in xy_dif and row+col not in xy_sum:
                    DFS(queues+[col], xy_dif+[row-col], xy_sum+[row+col])
        result = []
        DFS([], [], [])
        return [["." * i + "Q" + "." * (n-i-1) for i in row] for row in result]

