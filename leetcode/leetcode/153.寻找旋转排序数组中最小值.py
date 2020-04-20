class Solution:
    def findMin(self, nums):
        if len(nums) == 1:
            return nums[0]

        left, right = 0, len(nums)-1
        #单增情况
        if nums[right] > nums[0]:
            return nums[0]
        #二分查找：保留断层部分（断层有最值）
        while left <= right:
            mid = (left + right) // 2
            #1. nums[mid]处于断层处 456 123
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            if nums[mid] < nums[mid-1]:
                return nums[mid]

            #2. 搜索断层 456 123
            if nums[left] < nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

