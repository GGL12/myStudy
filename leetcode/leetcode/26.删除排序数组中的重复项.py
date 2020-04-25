class Solution:
    def removeDuplicates(self, nums):
        n = len(nums)
        #case
        if n == 0: return 0
        # i j 为两个指针,其中i还有计数功能
        i = 0
        for j in range(1, n):
            if nums[i] != nums[j]:
                i += 1
                #更新nums[i]的值，因为下一回合要比较这个索引的值
                nums[i] = nums[j]
        # +1是因为重复项也要算一个长度/全不为重复项时只循环了n-1次
        return i + 1