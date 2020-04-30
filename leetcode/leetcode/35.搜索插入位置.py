class Solution:
    def searchInsert(self, nums, target):
        '''
        两种二分查找,不要记错!!!!!
        '''
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left

    def binartSearch(self, nums, target):
        left, right = 0, len(nums) #注意
        while left < right: #注意
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid  #注意
            else:
                left = mid + 1
