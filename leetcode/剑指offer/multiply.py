class Solution:
    def multiply(self, A):
        # write code here
        m1 = []
        m2 = []
        ans1 = 1
        ans2 = 1
        res = []
        for i in range(len(A)):
            res.append(ans1)
            res.insert(0, ans2)
            ans1 *= A[i]
            ans2 *= A[len(A) - 1- i]
            i += 1
        return res
if __name__ == '__main__':
    A = [1, 2, 3, 4, 5]
    s = Solution()
    print(s.multiply(A))