class Solution:
    def threeSumClosest(self, nums, target):
        #赋初值
        res = float("inf")
        n = len(nums)
        nums = sorted(nums)
        #循环遍历数组
        for i in range(n):
            left = i + 1
            right = n - 1
            while left < right:
                value = nums[i] + nums[left] + nums[right]
                #最接近目标值
                if abs(target - value) < abs(target - res):
                    res = value
                #case
                if value > target: right -= 1
                elif value < target: left += 1
                else: return res
        return res
