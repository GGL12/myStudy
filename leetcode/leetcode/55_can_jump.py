class Solution:
    def can_jump(self, nums):
        if len(nums) <= 1:
            return True
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            if dp[i-1] >= i:
                dp[i] = max(dp[i-1], i+nums[i])
            else:
                dp[i] = dp[i-1]
            if dp[i] >= len(nums) - 1:
                return True
        return False