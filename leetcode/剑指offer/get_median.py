# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        #初始化大堆/小堆以及大小堆的结点个数
        self.max_heap = []
        self.min_heap = []
        self.max_count = 0
        self.min_count = 0
    def insert(self, num):
        # 在插入数据的过程中，根据个数插入不同的堆中，同时比较堆顶点
        if self.max_count > self.min_count:
            self.min_count += 1
            if num < self.max_heap[0]:
                tmp_num = self.max_heap[0]
                self.max_heap[0] = num
                self.adjust_heap(self.max_heap, self.cmp_max)
                self.create_heap(tmp_num, self.min_heap, self.cmp_min)
            else:
                self.create_heap(num, self.min_heap, self.cmp_min)
        else:
            self.max_count += 1
            if not self.max_heap:
                self.max_heap.append(num)
            else:
                if num > self.min_heap[0]:
                    tmp_num = self.min_heap[0]
                    self.min_heap[0] = num
                    self.adjust_heap(self.min_heap, self.cmp_min)
                    self.create_heap(tmp_num, self.max_heap, self.cmp_max)
                else:
                    self.create_heap(num, self.max_heap, self.cmp_max)
    def get_median(self):
        # write code here
        if self.max_count > self.min_count:
            return self.max_heap[0]
        else:
            return (self.max_heap[0] + self.min_heap[0]) / 2.0
    def adjust_heap(self, heap, cmp_fun):
        cur_index = 0
        cmp_index = 0
        while cur_index < len(heap):
            left_index = cur_index * 2 + 1
            right_index = left_index + 1
            if right_index < len(heap):
                cmp_index = left_index if cmp_fun(heap[left_index], heap[right_index]) else right_index
            elif left_index < len(heap):
                cmp_index = left_index
            else:
                break
            if cmp_fun(heap[cmp_index], heap[cur_index]):
                heap[cur_index], heap[cmp_index] = heap[cmp_index], heap[cur_index]
            cur_index = cmp_index
    def create_heap(self, num, heap ,cmp_fun):
        heap.append(num)
        cur_index = heap.index(num)
        while cur_index != 0:
            par_index = (cur_index - 1) // 2
            if cmp_fun(heap[cur_index], heap[par_index]):
                heap[cur_index], heap[par_index] = heap[par_index], heap[cur_index]
                cur_index = par_index
            else:
                break
    def cmp_max(self, val1, val2):
        return val1 > val2
    def cmp_min(self, val1, val2):
        return val1 < val2

if __name__ == '__main__':
    s = Solution()
    for i in [5,2,3,4,1,6,7,0,8]:
        s.insert(i)
        print(s.get_median())

# class Solution:
#     def __init__(self):
#         self.little_value_max_heap = []
#         self.big_value_min_heap = []
#         self.max_heap_count = 0
#         self.min_heap_count = 0
#
#     def Insert(self, num):
#         # write code here
#         if self.max_heap_count > self.min_heap_count:
#             self.min_heap_count += 1
#             if num < self.little_value_max_heap[0]:
#                 tmp_num = self.little_value_max_heap[0]
#                 self.adjust_max_heap(num)
#                 self.create_min_heap(tmp_num)
#             else:
#                 self.create_min_heap(num)
#         else:
#             self.max_heap_count += 1
#             if len(self.little_value_max_heap) == 0:
#                 self.create_max_heap(num)
#             else:
#                 if self.big_value_min_heap[0] < num:
#                     tmp_num = self.big_value_min_heap[0]
#                     self.adjust_min_heap(num)
#                     self.create_max_heap(tmp_num)
#                 else:
#                     self.create_max_heap(num)
#
#     def GetMedian(self):
#         # write code here
#         if self.min_heap_count < self.max_heap_count:
#             return self.little_value_max_heap[0]
#         else:
#             return (self.little_value_max_heap[0] + self.big_value_min_heap[0]) / 2
#
#     def create_max_heap(self, num):
#         self.little_value_max_heap.append(num)
#         current_index = self.little_value_max_heap.index(num)
#         while current_index != 0:
#             parent_index = (current_index - 1) // 2
#             if self.little_value_max_heap[parent_index] < self.little_value_max_heap[current_index]:
#                 self.little_value_max_heap[parent_index], self.little_value_max_heap[current_index] = \
#                     self.little_value_max_heap[current_index], self.little_value_max_heap[parent_index]
#                 current_index = parent_index
#             else:
#                 break
#
#     def adjust_max_heap(self, num):
#         if num < self.little_value_max_heap[0]:
#             max_heap_len = len(self.little_value_max_heap)
#             self.little_value_max_heap[0] = num
#             index = 0
#             larger_index = 0
#             while index < max_heap_len:
#                 left_index = index * 2 + 1
#                 right_index = left_index + 1
#                 larger_index = 0
#                 if right_index < max_heap_len:
#                     larger_index = right_index if self.little_value_max_heap[left_index] < self.little_value_max_heap[
#                         right_index] else left_index
#                 elif left_index < max_heap_len:
#                     larger_index = left_index
#                 else:
#                     break
#                 if self.little_value_max_heap[index] < self.little_value_max_heap[larger_index]:
#                     self.little_value_max_heap[index], self.little_value_max_heap[larger_index] = \
#                         self.little_value_max_heap[larger_index], self.little_value_max_heap[index]
#                 index = larger_index
#
#     def create_min_heap(self, num):
#         self.big_value_min_heap.append(num)
#         current_index = self.big_value_min_heap.index(num)
#         while current_index != 0:
#             parent_index = (current_index - 1) // 2
#             if self.big_value_min_heap[current_index] < self.big_value_min_heap[parent_index]:
#                 self.big_value_min_heap[parent_index], self.big_value_min_heap[current_index] = \
#                     self.big_value_min_heap[current_index], self.big_value_min_heap[parent_index]
#                 current_index = parent_index
#             else:
#                 break
#
#     def adjust_min_heap(self, num):
#         if num < self.big_value_min_heap[0]:
#             min_heap_len = len(self.big_value_min_heap)
#             self.big_value_min_heap[0] = num
#             index = 0
#             larger_index = 0
#             while index < min_heap_len:
#                 left_index = index * 2 + 1
#                 right_index = left_index + 1
#                 smaller_index = 0
#                 if right_index < min_heap_len:
#                     smaller_index = right_index if self.big_value_min_heap[right_index] < self.big_value_min_heap[
#                         left_index] else left_index
#                 elif left_index < min_heap_len:
#                     smaller_index = left_index
#                 else:
#                     break
#                 if self.big_value_min_heap[smaller_index] < self.big_value_min_heap[index]:
#                     self.big_value_min_heap[index], self.big_value_min_heap[smaller_index] = \
#                         self.big_value_min_heap[smaller_index], self.big_value_min_heap[index]
#                 index = smaller_index
#
#
# if __name__ == '__main__':
#     s = Solution()
#     for i in [5, 2, 3, 4, 1, 6, 7, 0, 8]:
#         s.Insert(i)
#         print(s.GetMedian())