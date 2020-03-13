'''
    动态规划:    1. 确定状态
                2. 转移方程
                3. 初始条件和边界情况
                4. 计算顺序
'''
class Solution:
    # def coin_change(self, coins, amount):
    #     res = [float('inf')] * (amount + 1)
    #     #initialization 零枚硬币零次
    #     res[0] = 0
    #     for i in range(1, amount+1):
    #         for c in coins:
    #             #判断边际
    #             if (i - c >= 0) and res[i - c] != float('inf'):
    #                 res[i] = min(res[i-c] + 1, res[i])
    #
    #     return -1 if res[amount] == float('inf') else res[amount]

    def coinChange(self, coins, amount):
        res = [0] * (amount + 1)
        for i in range(1, amount+1):
            cost = float('inf')
            for c in coins:
                if i - c >= 0:
                    cost = min(cost, res[i-c]+1)
            res[i] = cost

        return -1 if res[-1] == float('inf') else res[-1]