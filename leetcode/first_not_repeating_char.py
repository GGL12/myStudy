class Solution:
    def first_not_repeating_chat(self, s):
        if not s:
            return -1
        hash_list = [0] * 256
        for str in s:
            hash_list[ord(s)] += 1
        for i in range(len(s)):
            if hash_list[ord(s[i])] == 1:
                return i