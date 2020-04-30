from collections import defaultdict
class Solution:
    def solveSudoku(self, board):
        self.initialize(board)
        self.backtrack()
    def initialize(self, board):
        '''
        初始化数独棋盘
        :param board:
        :return:
        '''
        self.board = board
        #待填充的位置
        self.locs = []
        #记录行竖小格的数字
        self.rowMap = [defaultdict(int)] * 9
        self.colMap = [defaultdict(int)] * 9
        self.blockMap = [defaultdict(int)] * 9
        #开始记录
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == '.':
                    self.locs.append((row, col))
                else:
                    num = int(self.board[row][col])
                    blockIdx = (row // 3) * 3 + col // 3
                    self.rowMap[row][num] += 1
                    self.colMap[col][num] += 1
                    self.blockMap[blockIdx][num] += 1
    def backtrack(self):
        #结束条件
        if not self.locs:
            return True
        #弹出当前要填的位置
        row, col = self.locs.pop()
        blockIdx = (row // 3) * 3 + col // 3
        found = False
        #开始扫描
        for num in range(1, 10):
            if found: break
            #如果当前数字都没有出现过
            if not self.rowMap[row][num] and not self.colMap[col][num] and not self.blockMap[blockIdx][num]:
                #开始操作
                self.rowMap[row][num] = 1
                self.colMap[col][num] = 1
                self.blockMap[blockIdx][num] = 1
                self.board[row][col] = str(num)
                #递归到下一层填充
                found = self.backtrack()
                #状态回溯，将填充的位置清空
                self.rowMap[row][num] = 0
                self.colMap[col][num] = 0
                self.blockMap[blockIdx][num] = 0
        #如果本轮无法求解，回溯到初始状态，继续从前面填充
        if not found:
            self.locs.append((row, col))
            self.board[row][col] = '.'
        return found




