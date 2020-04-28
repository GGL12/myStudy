class Solution:
    def nextPermutation(self, nums):
        '''
        1. 从后序遍历，找到非递增的点minPosition - 1
        2. 在[minPosition: -1]中从后序找到比minPosition-1值大的点(maxPosition)交换
        3. 至此[minPosition: -1] 为递减的序列，将其变为递增
        '''
        n = len(nums)
        #case
        if n < 2: return 0
        #赋初值
        minPosition = maxPosition = n - 1
        #找到minPosition位置，minPosition-1为交换的点
        while minPosition > 0 and nums[minPosition-1] >= nums[minPosition]:
            minPosition -= 1
        #若minPosition=0表明数组递减，则返回翻转数组
        if minPosition == 0:
            return nums.reverse()
        else:
            #从[minPosition: -1]找到大于交换点的值
            while maxPosition > minPosition - 1 and nums[maxPosition] <= nums[maxPosition-1]:
                maxPosition -= 1
            #交换两点 至此[minPosition: -1]递减
            nums[minPosition-1] , nums[maxPosition] = nums[maxPosition], nums[minPosition-1]
            #[minPosition: -1] 变为递增
            for i in range((n - minPosition) // 2):
                nums[minPosition + i], nums[n - 1 - i] = nums[n - 1 - i], nums[minPosition + i]
