class Solution:
    def number_of_one(self, n):
        '''
        count = 0
        for i in range(32):
            mask = 1 << i
            if n & mask != 0:
                count += 1
        return count
        '''
        count = 0
        while n:
            n = n & (n - 1)
            count += 1
        return count