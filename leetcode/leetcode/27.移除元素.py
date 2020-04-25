class Solution:
    def removeElement(self, nums, val):
        #赋初值
        n = len(nums)
        #i, j 为两个指针
        i = 0
        for j in range(n):
            if nums[j] != val:
                #将不相等的值往前面放
                nums[i] = nums[j]
                #计数 and 为下一个不相等元素预留位置
                i += 1
        return i
    def fun2(self, nums, val):
        n = len(nums)
        #i n为两个指针，i是不相等的值存放位置，n不断交换
        i = 0
        while i < n:
            if nums[i] == val:
                nums[i] = nums[n-1]
                n -= 1
            else:
                i += 1
        return n