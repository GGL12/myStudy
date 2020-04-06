from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[str]:
        '''
        方法一：排序数组分类
    思路
    当且仅当它们的排序字符串相等时，两个字符串是字母异位词
        '''
        res = defaultdict(list)
        for s in strs:
            res[tuple(sorted(s))].append(s)
        return list(res.values())
    def fun2(self, strs):
        '''
         方法二：按计数分类
        思路
        当且仅当它们的字符计数（每个字符的出现次数）相同时，两个字符串是字母异位词。
        '''
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())

