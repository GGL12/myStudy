class Solution:
    def combinationSum(self, condidates, target):

        def backtrack(condidates, begin, end, path, res, target):
            '''
            回溯+剪枝
            :param condidates:
            :param begin:
            :param end:
            :param path:
            :param res:
            :param target:
            :return:
            '''
            #结束条件
            if target == 0:
                #路径添加到结果中
                res.append(path[:])
                return
            #循环操作元素
            for i in range(begin, end):
                #新的目标值
                residue = target - condidates[i]
                #小于零 over
                if residue < 0:
                    break
                path.append(condidates[i])
                #递归到下一个路径
                backtrack(condidates, i, end, path, res, residue)
                #回溯到上一层
                path.pop()
        end = len(condidates)
        if end == 0: return []
        #剪枝是为了提速，在本题非必需
        condidates.sort()
        res = []
        path = []
        backtrack(condidates, 0, end, path, res, target)
        return res