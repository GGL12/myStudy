class Solution:
    def get_least_numbers(self, tinput, k):
        self.max_heap = []
        self.input_len = len(tinput)
        # 判断边际
        if self.judge_input(tinput, k):
            for i in range(self.input_len):
                if i < k:
                    self.create_max_heap(tinput[i])
                else:
                    self.adjust_max_heap(tinput[i])
            return sorted(self.max_heap)
        else:
            return []

    def judge_input(self, tinput, k):
        '''
            判断初始化的输入
        '''
        if self.input_len < k or k <= 0:
            return []
        return tinput

    def create_max_heap(self, num):
        '''
            求k个最小值，构建k结点的最大堆
        '''
        self.max_heap.append(num)
        current_index = self.max_heap.index(num)
        while current_index != 0:
            parent_index = (current_index - 1) // 2
            if self.max_heap[parent_index] < self.max_heap[current_index]:
                current_index = parent_index
                self.max_heap[parent_index], self.max_heap[current_index] = self.max_heap[current_index], self.max_heap[parent_index]
            else:
                break
    def adjust_max_heap(self, num):
        '''
            不断加入新的数组，判断是否大于根结点，然后更新最大堆
        '''
        if num < self.max_heap[0]:
            self.max_heap[0] = num
            index = 0
            length = len(self.max_heap)
            while index < length:
                child_left = index * 2 + 1
                child_right = child_left + 1
                larger_index = 0
                if child_right < length:
                    if self.max_heap[child_right] < self.max_heap[child_left]:
                        larger_index = child_left
                    else:
                        larger_index = child_right
                elif child_left < length:
                    larger_index = child_left
                else:
                    break
                if self.max_heap[index] < self.max_heap[larger_index]:
                    self.max_heap[index] , self.max_heap[larger_index] = self.max_heap[larger_index], self.max_heap[index]
                index = larger_index




