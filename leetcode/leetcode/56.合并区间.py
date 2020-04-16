class Solution:
    def merge(self, intervals):
        res = []
        #按照起始升序
        intervals.sort(key = lambda x: x[0])
        for item in intervals:
            #如果列表为空，或者当前区间与上一区间不重合，直接添加
            if not res or item[1] > res[-1][1]:
                res.append(item)
            else:
                #否则和上一区间合并
                res[-1][1] = max(res[-1][1], item[1])
        return res