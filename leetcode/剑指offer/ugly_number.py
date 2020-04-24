class Solution:
    # def get_ugly_number(self, index):
    #     count = 0
    #     number = 1
    #     while True:
    #         if self.is_ugly_number(number):
    #             count += 1
    #         if count == index:
    #             return number
    #         number += 1
    #
    # def is_ugly_number(self, number):
    #     while number % 2 == 0:
    #         number //= 2
    #     while number % 3 == 0:
    #         number //= 3
    #     while number % 5 == 0:
    #         number //= 5
    #     if number == 1:
    #         return True
    #     else:
    #         return False
    def get_ugly_number(self, index):
        if index < 1:
            return 0
        count = 1
        ugly_list = [1]
        two_pointer = 0
        three_pointer = 0
        five_pointer = 0
        while count != index:
            cur_two_val = 2 * ugly_list[two_pointer]
            cur_three_val = 3 * ugly_list[three_pointer]
            cur_five_val = 5 * ugly_list[five_pointer]
            min_val = min(cur_two_val, cur_three_val, cur_five_val)
            ugly_list.append(min_val)
            if min_val == cur_two_val:
                two_pointer += 1
            if min_val == cur_three_val:
                three_pointer += 1
            if min_val == cur_five_val:
                five_pointer += 1
            count += 1
        return ugly_list[count - 1]




