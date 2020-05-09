class Solution:
    def findInMountainArray(self, target, mountain_arr):
        left, right = 0, mountain_arr.length() - 1
        # 找到山顶的索引
        while left < right:
            mid = (left + right) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                left = mid + 1
            else:
                right = mid
        peek = left
        # 前半部分查找
        targetIdx = self.binarySearch(mountain_arr, target, 0, peek)
        if targetIdx != -1: return targetIdx
        # 后半部分查找
        return self.binarySearch(mountain_arr, targetIdx, peek + 1, mountain_arr.length(), lambda x: -x)

    def binarySearch(self, mountain, target, left, right, key=lambda x: x):
        # 匿名函数取巧: 将逆序变升序，统一二分查找
        target = key(target)
        while left <= right:
            mid = (left + right) // 2
            cur = key(mountain.get(mid))
            if cur == target:
                return mid
            elif cur < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
