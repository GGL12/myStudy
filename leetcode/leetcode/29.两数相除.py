class Solution:
    def divide(self, dividend, divisor):
        #符号位判断
        sign = (dividend > 0) ^ (divisor > 0)
        #取绝对值
        dividend, divisor = abs(dividend), abs(divisor)
        #赋初值
        count = 0
        result = 0
        while dividend >= divisor:
            count += 1
            divisor <<= 1
        while count > 0:
            count -= 1
            divisor >>= 1
            if divisor <= dividend:
                result += 1 << count
                dividend -= divisor
        if sign: result = -result
        return result if -(1<<31) <= result <= (1<<31)-1 else (1<<31)-1