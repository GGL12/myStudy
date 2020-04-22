class Solution:
    def intToRoman(self, num):
        #贪心策略
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        idx = 0
        res = ""
        while idx < len(nums):
            #使用最大的面值,贪心的策略
            while num >= nums[idx]:
                res += romans[idx]
                num -= nums[idx]
            idx += 1
        return res