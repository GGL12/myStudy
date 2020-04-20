class Solution:
    def maxProduct(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        maxValue, iMax, iMin = nums[0]
        for i in range(1, n):
            if nums[i] < 0:
                iMax, iMin = iMin, iMax
            iMax = max(iMax*nums[i], nums[i])
            iMin = min(iMin*nums[i], nums[i])
            maxValue = max(iMax, maxValue)

        return maxValue