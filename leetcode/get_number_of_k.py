from collections import Counter
class Sulotion:
    # def get_number_of_k(self, data, k):
    #     if not data:
    #         return 0
    #     res = Counter(data).get(k)
    #     if not res:
    #         return 0
    #     return res
    def get_number_of_k(self, data, k):
        if not data: return 0
        return self.binary_search(data, k+.5) - self.binary_search(data, k-.5)
    def binary_search(self, data, k):
        low = 0
        high = len(data) - 1
        while low <= high:
            mid = (low + high) // 2
            if data[mid] > k:
                high = mid - 1
            elif data[mid] < k:
                low = mid + 1
        return high