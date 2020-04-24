class Solution:
    def add_two_num(self, num1, num2):
        max_num = 0X7FFFFFFF
        mask = 0XFFFFFFFF
        while num2 != 0:
            num1, num2 = (num1 ^ num2), ((num1 & num2) << 1)
            num1 = num1 & mask
            num2 = num2 & mask
        return num1 if num1 <= max_num else ~(num1 & mask)
