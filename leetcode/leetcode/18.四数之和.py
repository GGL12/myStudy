class Solution:
    def fourSum(self, nums, target):
        n = len(nums)
        res = []
        nums = sorted(nums)

        for i in range(n-3):
            #if nums[i] > target: break
            if i > 0 and nums[i] == nums[i-1]: continue
            for j in range(i+1, n-2):
                #if nums[j] > target-nums[i]: break
                if j > i + 1 and nums[j] == nums[j-1]: continue
                c = j + 1
                d = n - 1
                while c < d:
                    value = nums[i] + nums[j] + nums[c] + nums[d]
                    if value == target:
                        res.append([nums[i], nums[j], nums[c], nums[d]])
                        while c < d and nums[c] == nums[c+1]: c += 1
                        while c < d and nums[d] == nums[d-1]: d -= 1
                        c += 1
                        d -= 1
                    elif value > target: d -= 1
                    else: c += 1

        return res


class Solution:
    def fourSum(self, nums, target):
        n = len(nums)
        if n < 4:
            return []
        res = set()
        nums.sort()
        table = {}

        for i in range(n - 1):
            for j in range(i + 1, n):
                s = nums[i] + nums[j]
                if target - s in table:
                    for tem in table[target - s]:
                        if tem[1] < i:
                            res.add((nums[tem[0]], nums[tem[1]], nums[i], nums[j]))
                if s not in table:
                    table[s] = []
                table[s].append((i, j))

        ans = []
        for r in res:
            ans.append(list(r))
        return ans

s = Solution()
s.fourSum([1,0,-1,0,-2,2], 0)