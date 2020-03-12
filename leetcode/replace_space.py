class Solution:
    def replace_space(self, s):
        res = ""
        for c in s:
            if c.strip():
                res += c
            else:
                res += "%20"
        return res