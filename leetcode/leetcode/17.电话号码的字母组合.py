class Sulution:
    def letterCombinations(self, digits):
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        def backtrack(digits, cur):
            if len(digits) == 0:
                res.append(cur)
            else:
                for c in phone[digits[0]]:
                    backtrack(digits[1:], c+cur)
        res = []
        if digits:
            backtrack(digits, "")
        return res