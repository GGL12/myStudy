class Solution:
    def romanToInt(self, s):
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        hashMap = dict(zip(romans, nums))

        res = 0
        preNum = hashMap[s[0]]
        for i in range(1, len(s)):
            cur = hashMap[i]
            if preNum < cur:
                res -= preNum
            else:
                res += preNum
            preNum = cur
        res += preNum
        return res