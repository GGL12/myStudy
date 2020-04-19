class Solution:
    def searchMatrix(self, matrix, target):
        #二分查找
        #midValue = matrix[midIdx//col][midIdx%col]
        row = len(matrix)
        col = len(matrix[0])
        left, right = 0, row*col-1
        while left <= right:
            midIdx = (left + right) // 2
            midValue = matrix[midIdx//col][midIdx%col]
            if midValue == target:
                return True
            elif midValue > target:
                right = midIdx - 1
            else:
                left = midIdx + 1
        return False