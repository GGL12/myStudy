class Solution:
    def multiply(self, num1, num2):
        '''
        竖式乘法过程
        :param num1:
        :param num2:
        :return:
        '''
        def strToInt(s):
            return ord(s) - ord('0')
        res = 0
        for i, x in enumerate(num1[::-1]):
            tmp = 0
            for j, y in enumerate(num2[::-1]):
                tmp += strToInt(x) * strToInt(y) * 10**j
            res += tmp * 10**i
        return str(res)