class Solution:
    def mySqrt(self, x):
        #二分查找
        if x == 0 or x == 1:
            return x

        left, right = 1, x
        while left <= right:
            mid = (left + right) // 2
            if mid * mid > x:
                right = mid - 1
            else:
                left = mid + 1
        return right

    def fun2(self, x):
        #牛顿迭代法
        r = x
        while r * r > x:
            r = (r + r//x) // 2
        return r