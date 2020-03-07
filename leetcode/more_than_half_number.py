from collections import Counter
class Solution:
    def more_than_half_num(self, numbers):
        # nums_count = {}
        # nums_len = len(numbers)
        # for num in numbers:
        #     if num in nums_count:
        #         nums_count[num] += 1
        #     else:
        #         nums_count[num] = 1
        #
        #     if nums_count[num] >= (nums_len >> 1):
        #         return num
        # return 0
        nums_count = Counter(numbers)
        num, count = sorted(nums_count.items(), key=lambda x:x[1], reverse=True)[0]
        return num if count > (len(numbers) >> 1) else 0


