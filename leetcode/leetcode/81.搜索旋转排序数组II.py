class Solution:
    def search(self, nums, target):
        if not nums:
            return False

        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True

            #case 分不清是否有序
            if nums[left] == nums[mid]:
                left += 1
                continue
            #前部分有序
            if nums[left] < nums[mid]:
                #目标在有序数组里
                if nums[left] <= target and target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return False