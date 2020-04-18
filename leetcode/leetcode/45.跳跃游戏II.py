class Solution:
    def jump(self, nums):
        end = maxPosition = res = 0
        for i in range(len(nums)-1):
            maxPosition = max(maxPosition, nums[i]+i)
            if i == end:
                end = maxPosition
                res += 1
        return res