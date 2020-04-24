class Solution:
    def duplicate(self, numbers, duplication):
        map = [0] * 10
        for n in numbers:
            if map[n] == 1:
                duplication[0] = n
                return True
            else:
                map[n] += 1

        return False
