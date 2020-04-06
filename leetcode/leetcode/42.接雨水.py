class Solution:
    def trap(self, height: list[int]) -> int:
        """
        遍历每个数据，然后找到左右最高度，高度差大于当前值，则表明可以接水
        """
        res = 0
        n = len(height)
        for i in range(n):
            maxLeft, maxRight = 0, 0
            for j in range(0, i):
                maxLeft = max(maxLeft, height[j])
            for j in range(i, n):
                maxRight = max(maxRight, height[j])
            tmp = min(maxLeft, maxRight)
            if tmp > height[i]:
                res += tmp - height[i]
        return res
    def fun(self, height: list[int]) -> int:
        #使用dp优化
        res = 0
        n = len(height)
        maxLeft = [0] * n
        maxRight = [0] * n

        #初始化
        maxLeft[0] = height[0]
        maxRight[-1] = height[-1]
        for i in range(1, n):
            maxLeft[i] = max(maxLeft[i-1], height[i])
        for i in range(n-2, -1, -1):
            maxRight[i] = max(maxRight[i+1], height[i])

        for i in range(n):
            tmp = min(maxLeft[i], maxRight[i])
            if tmp > height[i]:
                res += tmp - height[i]
        return res

    def fun2(self, height: list[int]) -> int:
        """
        双指针法：分别向中间缩进，分别左右求解
        """
        res = 0
        n = len(height)
        left, right = 0, n-1
        maxLeft, maxRight = height[0], height[-1]

        while left <= right:
            maxLeft = max(height[left], maxLeft)
            maxRight = max(height[right], maxRight)
            if maxLeft < maxRight:
                res += maxLeft - height[left]
                left += 1
            else:
                res += maxRight - height[right]
                right -= 1
        return res
