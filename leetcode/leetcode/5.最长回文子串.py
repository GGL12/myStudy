class Solution:
    def longestPalindrome(self, s):
        #case为空
        if not s:
            return ""
        #初始化
        n = len(s)
        curLength = 1
        left = right = maxStart = maxLength = 0
        #中心扩散法
        for i in range(n):
            #左右初始化
            left = i - 1
            right = i + 1
            #左边与当前值相等
            while (left >= 0 and s[left] == s[i]):
                curLength += 1
                left -= 1
            #右边与当前值相等
            while (right < n and s[right] == s[i]):
                curLength += 1
                right += 1
            #左右两边值相等
            while (left >= 0 and right < n and s[left] == s[right]):
                curLength += 1
                left -= 1
                right += 1
            #更新最大子回文串起点和长度
            if curLength > maxLength:
                maxLength, maxStart = curLength, left
            #回文串长度归一
            curLength = 1
        return s[maxStart: maxStart+maxLength+1]

    def fun(self, s):
        '''
        动态规划
        '''
        if not s:
            return ""
        #初始化变量
        strLength = len(s)
        start = end = 0
        maxLength = 1
        dp = [[0] * strLength] * strLength
        #循环左右边界
        for right in range(1, strLength):
            for left in range(right):
                #更新条件左右字符相等时，right-left<=2(a,aba,aa) left+1 right-1也是回文串
                if s[left] == s[right] and (right - left <= 2 or dp[left+1][right-1] == 1):
                    #更新当前dp
                    dp[left][right] == 1
                    #更新最大回文串长度和开始结束标记
                    if (right - left + 1) > maxLength:
                        maxLength = right - left + 1
                        start, end = left, right
        return s[start: end+1]
