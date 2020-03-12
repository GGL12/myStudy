class Solution:
    def print_matrix(self, matrix):
        res = []
        while matrix:
            res += matrix.pop(0)
            if not matrix:
                break
            matrix = self.turn(matrix)
        return res
    def turn(self, matrix):
        row = len(matrix)
        col = len(matrix[0])
        new_matrix = []
        for i in range(col):
            new_line = []
            for j in range(row):
                new_line.append(matrix[j][col-1-i])
            new_matrix.append(new_line)
        return new_matrix
