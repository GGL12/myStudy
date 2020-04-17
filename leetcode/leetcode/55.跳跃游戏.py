class Solution:
    def canJump(self, nums):
        #贪心
        if not nums:
            return False
        end = len(nums) - 1
        for i in range(end, -1, -1):
            if nums[i] + i >= end:
                end = i
        return end == 0
