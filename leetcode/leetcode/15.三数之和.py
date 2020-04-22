class Solution:
    def threeSum(self, nums):
        '''
        排序+双指针
        '''
        #赋初值
        n = len(nums)
        res = []
        #case
        if n < 3: return res
        #排序数组
        nums = sorted(nums)
        for i in range(n):
            #结束条件
            if nums[i] > 0: break
            #去重
            if i > 0 and nums[i] == nums[i-1]: continue
            left = i + 1
            right = n - 1
            while (left < right):
                value = nums[i] + nums[left] + nums[right]
                if value == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    #去重左端数据
                    while left < right and nums[left] == nums[left+1]: left += 1
                    #去重有端数据
                    while left < right and nums[right] == nums[right-1]: right -= 1
                    left += 1
                    right -= 1
                #大于目标值，右移动
                elif value > 0: right -= 1
                #小于目标值，左移动
                else: left += 1
            return res