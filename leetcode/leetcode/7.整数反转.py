class Solution:
    def reverse(self, x):
        #case
        if -10 < x and x < 10:
            return x
        #转化为字符串
        strX = str(x)
        #判断是否负数
        if strX[0] != "-":
            x = int(strX[::-1])
        else:
            #去除“-”
            x = -int(strX[: 0: -1])
        return x if -2147483648 < x and x < 2147483647 else 0
    def fun(self, x):

        y, res = abs(x), 0
        boundry = (1 << 31) - 1 if x > 0 else (1 << 31)
        while y != 0:
            res = res * 10 + y % 10
            if res > boundry:
                return 0
            y //= 10
        return res if x > 0 else -res