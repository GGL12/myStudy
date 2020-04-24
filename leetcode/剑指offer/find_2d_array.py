class sulution:
    def find(self, target, array):
        '''
            1  2   3  4
            5  6   7  8
            9  10 11 12
            13 14 15 16
        '''
        # for i in range(len(array)):
        #     for j in range(len(array[i])):
        #         if target == array[i][j]:
        #             return True
        # O(n*m)
        # return False
        row_count = len(array)
        col_count = len(array[0])
        i = 0
        j = col_count - 1
        while i < row_count and j >= 0:
            value = array[i][j]
            if value == target:
                return True
            elif value > target:
                j -= 1
            else:
                i += 1
        return False
