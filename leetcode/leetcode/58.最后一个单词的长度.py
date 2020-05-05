class Solution:
    def lengthOfLastWord(self, s):
        res = 0
        idx = len(s) - 1
        while idx >= 0 and s[idx] == " ":
            idx -= 1
        while idx >= 0 and s[idx] != " ":
            idx -= 1
            res += 1
        return res