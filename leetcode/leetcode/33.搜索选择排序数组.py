class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            #如果匹配成功
            if nums[mid] == target:
                return True
            #[left mid] 单增
            if nums[left] <=  nums[mid]:
                #target在单增区域内
                if nums[left] <= target and target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            #[mid right]单增
            else:
                #target在单增区域
                if nums[mid] <= target  and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False