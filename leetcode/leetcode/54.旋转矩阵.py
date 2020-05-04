# 操作	代码
# 转置	matrix[:]=map(list,zip(*matrix))
# 顺时针旋转	matrix[:] = map(list,zip(*matrix[::-1]))
# 逆时针旋转	matrix =list(map(list,zip(*matrix)))[::-1]

# matrix = [[1, 2, 3], [1, 2, 3]]
# # matrix[:] = map(list, zip(*matrix))
# # matrix[:] = map(list, zip(*matrix[::-1]))
# # matrix = list(map(list,zip(*matrix)))[::-1]

class Solution:
    def spiralOrder(self, matrix):
        '''
        依次取第一行数据，让后再逆时针旋转
        :param matrix:
        :return:
        '''
        res = []
        while matrix:
            res += matrix.pop(0)
            matrix = list(map(list, zip(*matrix)))[::-1]
        return res
