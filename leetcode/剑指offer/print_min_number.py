import functools
class Solution:
    def print_min_number(self, numbers):
        if not numbers: return ""
        if len(numbers) == 1: return numbers[0]
        return "".join(sorted(numbers, key=functools.cmp_to_key(self.compare)))
    def compare(self, s1, s2):
        s1 = str(s1)
        s2 = str(s2)
        if s1 + s2 < s2 + s1:
            return -1
        elif s1 + s2 == s2 + s1
            return 0
        elif s1 + s2 > s2 + s1:
            return 1






