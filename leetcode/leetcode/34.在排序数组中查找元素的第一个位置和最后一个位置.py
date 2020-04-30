class Solution:
    def searchRange(self, nums, target):
        '''
        两遍暴力循环
        '''
        for i in range(len(nums)):
            if nums[i] == target:
                left = i
                break
        #这种语法还第一次学会 对于for、while、try语句，有问题才执行else的部分。
        else: return [-1, -1]

        for i in range(len(nums)-1, -1, -1):
            if nums[i] == target:
                right = i
                break
        return [left, right]
    
    def fun(self, nums, target):
        
        def binarySearch(nums, target, isLeft):
            left = 0
            right = len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] > target or (isLeft and target == nums[mid]):
                    right = mid
                else:
                    left = mid + 1
            return left
        leftIdx = binarySearch(nums, target, True)
        if leftIdx == len(nums) or nums[leftIdx] != target:
            return [-1, -1]

        print([leftIdx, binarySearch(nums, target, False)-1])
