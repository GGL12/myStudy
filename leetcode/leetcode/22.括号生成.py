class Solution:
    def generateParenthesis(self, n: int) -> list[str]:

        def generate(res=[]):
            if len(res) == 2*n:
                if valid(res):
                    ans.append(res)
            else:
                res.append('(')
                generate(res)
                res.pop()
                res.append(')')
                generate(res)
                res.pop()

        def valid(res):
            balance = 0
            for c in res:
                if c == '(':
                    balance += 1
                else:
                    balance -= 1
                if balance < 0:
                    return False
            return balance == 0

        ans = []
        generate()
        return ans

    def fun2(self, n):
        # 回溯法
        ans = []
        def backtrack(S="", left=0, rihgt=0):
            if len(S) == 2*n:
                ans.append(S)
                return
            if left < n:
                backtrack(S+"(", left+1, rihgt)
            if rihgt < left:
                backtrack(S+")", left, rihgt+1)
        backtrack()
        return ans

    def fun3(self, n):
        #按括号序列的长度递归
        if n == 0:
            return [""]
        ans = []
        for c in range(n):
            for left in self.fun3(c):
                for right in self.fun3(n-1-c):
                    ans.append("({}){}".format(left, right))
        return ans

