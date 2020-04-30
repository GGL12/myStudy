
class Solution:
    def isValidSudoku(self, board):
        #赋初值
        rows = [{}] * len(board)
        cols = [{}] * len(board)
        boxes = [{}] * len(board)
        #循环遍历记录
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] != '.':
                    num = int(board[i][j])
                    boxIdx = (i // 3) * 3 + j // 3
                    #更新结果
                    rows[i][num] = rows[i].get(num, 0) + 1
                    cols[j][num] = cols[j].get(num, 0) + 1
                    boxes[boxIdx][num] = boxes[boxIdx].get(num, 0) + 1
                    #判断是否有出现重复的值
                    if rows[i][num] > 1 or cols[j][num] > 1 or boxes[boxIdx][num] > 1:
                        return False
        return True
