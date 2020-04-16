class Solution:
    def minMutation(self, start, end, bank):
        if end not in bank:
            return -1
        bank = set(bank)
        change = change = {"A": "TCG", "T": "ACG", "C": "ATG", "G": "ATC"}
        queue = [(start, 0)]

        while queue:
            cur, count = queue.pop(0)
            if cur == end:
                return count
            for idx, item in enumerate(cur):
                for char in change[item]:
                    tmp = cur[:idx] + char + cur[idx+1:]
                    if tmp in bank:
                        queue.append((tmp, count+1))
                        bank.remove(tmp)
        return -1