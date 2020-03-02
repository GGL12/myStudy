class Solution:
    def min_number_in_ratate_array(self, rotate_array):
        # min_num = 0
        # for i in range(len(rotate_array)):
        #     min_num = min_num if min_num < rotate_array[i] and min_num !=0 else rotate_array[i]
        # return min_num

        #最小值一定要比前面的要小
        #二分法查找数据，找左右的方法是：中值小于右边的值，就说明最小值在左边
        if not rotate_array:
            return 0
        left = 0
        right = len(rotate_array) - 1
        while left <= right:
            mid = (left + right) >> 1
            if rotate_array[mid] < rotate_array[mid-1]:
                return rotate_array[mid]
            elif rotate_array[mid] < rotate_array[right]:
                right = mid - 1
            else:
                left = mid + 1
        return 0