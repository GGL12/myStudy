class Solution:
    def is_continuous(self, numbers):
        if not numbers:
            return False

        jokers = 0
        cnt = 0
        pre = None
        for i in range(len(numbers)):
            if pre == None:
                pre = numbers[i]
            else:
                if numbers[i] == 0:
                    jokers += 1
                else:
                    if pre == numbers[i]:
                        return False
                    else:
                        cnt = pre - numbers[i] - 1
                        pre = numbers[i]
        cnt -= jokers
        return cnt <= 0