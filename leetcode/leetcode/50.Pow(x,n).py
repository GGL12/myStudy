class Solution:
    def myPow(self, x, n):
        def fastPow(x, n):
            if n == 0:
                return 1
            half = fastPow(x, x >> 1)
            if n % 2 == 0:
                return half * half
            else:
                return half * half * x
        if n < 0:
            x = 1/x
            n = -n
        return fastPow(x, n)

    def fun2(self, x, n):
        #快速幂循环
        if n < 0:
            n = -n
            x = 1/x
        res = 1
        while n != 0:
            if n & 1 != 0:
               res *= x
            x *= x
            n >>= 1
        return res