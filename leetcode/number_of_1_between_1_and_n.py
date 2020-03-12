class Solution:
    def NumberOf1Between1AndN_Solution(self, n):

        # write code here
        # def count_one(n):
        #     count = 0
        #     while n:
        #         if (n % 10 == 1):
        #             count += 1
        #         n /= 10
        #     return count
        #
        # res = 0
        # for i in range(1, n + 1):
        #     res += count_one(i)
        # return res
        count = 0
        i = 1
        while i <= n:
            a = n / i
            b = n % i
            count += (a + 8) / 10 * i + (a % 10 == 1) * (b + 1)
            i *= 10
        return count

