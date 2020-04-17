class Solution:
    def lemonadeChange(self, bills):
        #贪心算法，对于20元，优先找10+5的零钱
        five = ten = 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                #如果没有5块，返回False
                if not five: return False
                ten += 1
                five -= 1
            else:
                #对于20情况，优先找回10+5的零钱情况
                if ten and five:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True