
class Solution:
    def longestCommonPrefix(self, strs):
        #水平扫描法
        if not strs: return ""
        if len(strs) == 1: return strs[0]

        res = ""
        for i in range(len(strs[0])):
            for j in range(1, len(strs)): #扫描整个字符
                if i >= len(strs[j]) or strs[i] != strs[j][i]:
                    return res
            res += strs[0][i]
        return res
