from collections import defaultdict
class Solution:
    def majortyElement(self, nums):
        #hash表
        hashTable = defaultdict(int)
        for num in nums:
            hashTable[num] += 1
            if hashTable[num] >= len(nums) / 2:
                return num

    def fun2(self, nums):
        #排序，index=n/2的一定是众数
        nums = sorted(nums)
        return nums[len(nums) // 2]

    def fun3(self, nums):
        #Boyer-Moore 投票算法
        #众数为1， 非众数为-1
        count = 0
        condidate = None
        for num in nums:
            if count == 0:
                condidate = num
            count += (1 if condidate == num else -1)
        return condidate