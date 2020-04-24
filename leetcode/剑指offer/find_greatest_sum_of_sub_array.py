class sulution:
    def find_greatest_sum_of_sub_array(self, array):
        max_num = None
        tmp_num = 0
        for i in array:
            if max_num == None:
                max_num = i
            if tmp_num + i < i:
                tmp_num = i
            else:
                tmp_num += i
            if max_num < tmp_num:
                max_num = tmp_num
        return max_num




