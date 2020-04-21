class Solution:
    def lengthOfLongestSubstrig(self, s):
        if not s:
            return 0
        #初始化一个窗口和最大字符串
        window = []
        maxLength = 0
        #对每一个 字符遍历
        for c in s:
            #不在窗口则添加字符进去
            if c not in window:
                window.append(c)
            else:
                #在窗口里面，去除字符之前的字符串，并在后面添加当前字符
                window[:] = window[window.index(c)+1 :]
                window.append(c)
            #更新最大字符
            maxLength = max(maxLength, len(window))
        #处理无重复字符数据
        return maxLength if maxLength != 0 else len(s)

    def fun2(self, s):
        #双指针法 left right 表示窗口边界
        maxLength = left = right = 0
        for c in s:
            #如果char不在窗口，更新右边界
            if c not in s[left:right]:
                right += 1
            else:
                #如果在的话，更新left right边界
                left += s[left:right].index(c) + 1
                right += 1
            #更新最大字符串长度
            maxLength = max(maxLength, (right-left))
        #case全无重复数字情况
        return maxLength if maxLength != 0 else len(s)

[[0] * (3)] * 3