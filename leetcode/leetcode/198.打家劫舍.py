class Solution:
    def rpb(self, nums):
        n = len(nums)
        if n == 0:
            return 0

        dp = [0] * (n+1)
        dp[1] = nums[0]
        for i in range(1, n+1):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i-1])
        return dp[-1]
