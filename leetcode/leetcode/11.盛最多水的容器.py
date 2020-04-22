class Solution:
    def maxArea(self, height):
        #双指针法
        left, right = 0, len(height)-1
        res = 0
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            res = max(area, res)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return res