class Solution:
    def combinationSum2(self, candidates, target):
        '''
        回溯+剪枝
        :param candidates:
        :param target:
        :return:
        '''
        def backtrack(begin, path, target):
            #结果加入条件
            if target == 0:
                res.append(path[:])
            #循环数字加入到路径
            for i in range(begin, n):
                #剪枝操作
                if candidates[i] > target:
                    break
                #剪枝操作
                if i > begin and candidates[i-1] == candidates[i]:
                    continue
                #路径添加
                path.append(candidates[i])
                target -= candidates[i]
                #递归到探索
                backtrack(i+1, path, target)
                #回溯
                path.pop()
        #赋初值
        res = []
        n = len(candidates)
        if n == 0: return res
        candidates.sort()
        backtrack(0, [] , target)
        return res


