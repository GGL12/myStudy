class Solution:
    def sortColors(self, nums):
        # 使用三指针，怕p1指向1的最有，p2指向2的最左，cur指向当前的数据
        p1, p2, cur = 0, len(nums) - 1, 0
        while cur <= p2:
            if nums[cur] == 0:
                nums[p1], nums[cur] = nums[cur], nums[p1]
                p1 += 1
                cur += 1
            elif nums[cur] == 2:
                nums[p2], nums[cur] = nums[cur], nums[p2]
                p2 -= 1
            else:
                cur += 1
