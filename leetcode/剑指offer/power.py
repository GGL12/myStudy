class Solution:
    def power(self, base, exponent):
        flag = 1
        if not base:
            return False
        if not exponent:
            return 1
        if exponent < 1:
            flag = 0
        res = 1
        for i in range(abs(exponent)):
            res *= base
        if flag == 0:
            return 1 / res
        return res