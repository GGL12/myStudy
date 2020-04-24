class Solution:
    def jump_floor(self, number):
        # 1 - 1, 2 - 2, 3-3 4-5
        if number < 1:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2
        ret = 0
        a = 1
        b = 2
        for i in range(3, number+1):
            ret = a + b
            a = b
            b = ret
        return ret
    def jump_floor_2(self, number):
        #1-1, 2-2, 3-3, 4-8  2^n-1
        #f(n) = f(n-1) + f(n-2).....+f(1)
        #f(n-1) = f(n-2) + ....+f(1)
        #f(n) = 2f(n-1) n>1
        #(1) = 1 n=1
        if number == 1:
            return 1
        ret = 1
        a = 1
        for i in range(2, number+1):
            ret = 2 * a
            a = ret
        return ret
        #return pow(2, number-1)
if __name__ == "__main__":
    s = Solution()
    print(s.jump_floor(100))

