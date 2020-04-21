class Solution:
    def convert(self, s, numRows):
        #case
        if numRows < 2: return s

        #初始化
        res = [""] * numRows
        idx, flag = 0, -1
        for c in s:
            res[idx] += c
            if idx == 0 or idx == numRows-1:
                flag *= -1
            idx += flag
        return "".join(res)
