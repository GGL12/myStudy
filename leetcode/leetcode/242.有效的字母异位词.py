from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #排序后，比较是否相对
        return sorted(s) == sorted(t)
    def fun1(self, s: str, t: str) -> bool:
        #哈希
        if len(s) != len(t):
            return False
        # counter = [0] * 26
        # for i in range(len(s)):
        #     counter[ord(s[i]) - ord('a')] += 1
        #     counter[ord(t[i]) - ord('a')] -= 1
        # for i in range(26):
        #     if counter[i] != 0:
        #         return False
        # return True
        dicts = defaultdict(int)
        for i in range(len(s)):
            dicts[s[i]] += 1
            dicts[t[i]] -= 1

        for val in dicts.values():
            if val != 0:
                return False
        return True

    def fun2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        se = set(s)
        if len(se) == set(t):
            for i in se:
                if s.count(i) != t.count(i):
                    return False
                else:
                    return True
        else:
            return False

