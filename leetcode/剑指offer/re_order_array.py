class Solution:
    #时间复杂度o(n)
    #空间复杂度o(n)
    def re_order_array(self, array):

        ret = []
        for i in array:
            if i % 2 == 1:
                ret.append(i)
        for i in array:
            if i % 2 == 0:
                ret.append(i)
        return ret
