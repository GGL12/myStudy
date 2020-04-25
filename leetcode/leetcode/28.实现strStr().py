class Solution:
    def strStr(self, haystack, needle):
        #线性滑动窗口 o((l-n)*n)
        l, n = len(haystack), len(needle)
        for start in (l - n + 1):
            if haystack[start: start+n] == needle:
                return start
        return -1