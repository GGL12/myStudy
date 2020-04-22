class Solution:
    def isMatch(self, s, p):
        '''
        递归
        '''
        #递归终止条件，都为空时,返回True
        if not p: return not s
        #匹配第一个字符 case1:s p第一个字符相等 case2:遇到"."任意匹配
        firstMatch = bool(s) and p[0] in [s[0], "."]
        #处理"*"问题:至少两个字符且后一个为"*"才能起作用。
        if len(p) >= 2 and p[1] == "*":
            #case1: *无用
            #case2: *匹配成功一个，移动s
            return self.isMatch(s, p[2:]) or (firstMatch and self.isMatch(s[1:], p))
        else:
            return firstMatch and self.isMatch(s[1:], p[1:])

    def fun2(self, s, p):
        '''
        动态规划
        '''
        dp = [[False] * (len(p) + 1)] * (len(s) + 1)
        for i in range(len(s), -1, -1):
            for j in range(len(p)-1, -1, -1):
                firstMatch = i < len(s) and p[j] in [s[i], "."]
                if j + 1 < len(p) and p[j+1] == "*":
                    dp[i][j] = dp[i][j+2] or (firstMatch and dp[i+1][j])
                else:
                    dp[i][j] = firstMatch and dp[i+1][j+1]

        return dp[0][0]
    
