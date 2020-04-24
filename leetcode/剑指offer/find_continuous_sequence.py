class Solution:
    def find_continuous_sequence(self, tsum):
        # res = []
        # one_res = []
        # sum = 0
        # num = 1
        # while num < tsum:
        #     if sum + num == tsum:
        #         one_res.append(num)
        #         res.append(one_res[:])
        #         sum += num
        #         num += 1
        #     elif sum + num < tsum:
        #         sum += num
        #         one_res.append(num)
        #         num += 1
        #     else:
        #         sum -= one_res.pop(0)
        # return res
        res = []
        windows = []
        sum = 0
        for num in range(1, tsum):
            windows.append(num)
            sum += num
            while sum > tsum:
                sum -= windows.pop(0)
            if sum == tsum:
                res.append(windows[:])
        return res

if __name__ == '__main__':
    target = 9
    s = Solution()
    print(s.find_continuous_sequence(target))