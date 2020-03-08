from collections import Counter
class Solution:
    # def find_nums_appear_once(self, array):
    #     nums_count = sorted(Counter(array).items(), key=lambda x: x[1])
    #     return nums_count[0][1], nums_count[1][0]

    def find_nums_appear_once(self, array):
        if len(array) < 2:
            return None

        #将所有的数字xor操作
        all_num_xor = None
        for num in array:
            if all_num_xor == None:
                all_num_xor = num
            else:
                all_num_xor ^= num
        #找到两个只出现一次数的某位不同
        count = 0
        while all_num_xor % 2 == 0:
            all_num_xor >>= 1
            count += 1
        mask = 1 << count

        #根据某位不同进行分组，然后xor运算得出两个不同的数
        first_num = None
        second_num = None
        for num in array:
            if mask & num == 0:
                if first_num == None:
                    first_num = num
                else:
                    first_num ^= num
            else:
                if second_num == None:
                    second_num = num
                else:
                    second_num ^= num
        return [first_num, second_num]



