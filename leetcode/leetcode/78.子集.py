class Sulution:
    def subsets(self, nums):
        def backtrack(first=0, cur=[]):
            if len(cur) == k:
                res.append(cur[:])
            for i in range(first, n):
                cur.append(nums[i])
                backtrack(i+1, cur)
                cur.pop()
        n = len(nums)
        res= []
        for k in range(n+1):
            backtrack()
        return res

    def fun2(self, nums):
        #迭代
        res = [[]]
        for num in nums:
            res += [[num] + cur for cur in res]
        return res

    def fun3(self, nums):
        if not nums:
            return []
        res = []
        n = len(nums)
        def helper(idx, tmp):
            res.append(tmp)
            for i in range(idx, n):
                helper(i+1, tmp+[nums[i]])
        helper(0, [])
        return res