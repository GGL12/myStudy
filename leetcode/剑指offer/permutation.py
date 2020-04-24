class Solution:
    def permutation(self, ss):
        if not ss:
            return []
        res = []
        self.perm(ss, res, "")
        return sorted(list(set(res)))

    def perm(self, ss, res, path):
        if not ss:
            res.append(path)
        else:
            for i in range(len(ss)):
                self.perm(ss[:i]+ss[i+1:], res, path+ss[i])

