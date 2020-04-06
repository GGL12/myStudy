class Solution:
    def twoSun(self, nums: list[int], target: int) -> list[int]:
        '''
        暴力解决 O(n^2)
        '''
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i,j]
                    break
                else:
                    continue
    def fun2(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        for i in range(n):
            a = target - nums[i]
            if a in nums:
                j = nums.index(a)
                if i == j:
                    continue
                else:
                    return [i, j]
                    break
            else:
                continue
    def fun3(self, nums: list[int], target: int) ->int:
        d = dict()
        n = len(nums)
        for i in range(n):
            if target - nums[i] in d.keys():
                return [d[target - nums[i]], i]
                break
            else:
                d[nums[i]] = i
    def fun4(self, nums: list[int], target: int) ->list[int]:
        hashmap = {}
        for idx, num in enumerate(nums):
            hashmap[num] = idx
        for idx, num in enumerate(nums):
            j = hashmap.get(target - num)
            if not j and idx != j:
                return [idx, j]
