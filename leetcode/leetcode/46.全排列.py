class Solution:
    def permute(self, nums):
        #回溯
        def backtrack(nums, tmp):
            if not nums:
                res.append(tmp)
                return
            for i in range(len(nums)):
                backtrack(nums[i:]+nums[i+1], tmp+[nums[i]])
        res = []
        backtrack(nums, [])
        return res
    def fun2(self, nums):
        def backtrack(first=0):
            if first == n:
                res.append(nums[:])
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first+1)
                nums[first], nums[i] = nums[i], nums[first]
        n = len(nums)
        res = []
        backtrack()
        return res
