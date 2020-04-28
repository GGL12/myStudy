class Solution:
    def numberOfSubarrays(self, nums, k):
        #赋初值
        n = len(nums)
        #处理边界
        array = [-1]
        res = 0
        #标记奇数的下标
        for i in range(n):
            if nums[i] % 2 == 1:
                array.append(i)
        #处理边界
        array.append(n)
        #[i, i+k-1] 包含k个奇数
        # array[i] - array[i-1]为起始奇数前面有多少偶数
        # array[i+k] - array[i+k-1]为结束奇数后面有多少个偶数
        for i in range(1, len(array)-k):
            res += (array[i] - array[i-1]) * (array[i+k] - array[i+k-1])
        return res
