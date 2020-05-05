class Solution:
    def insert(self, intervals, newInterval):
        #初始化变量
        inStart, inEnd = newInterval
        idx, n = 0, len(intervals)
        res = []
        #将插入之前的数据加入到结果集中
        while idx < n or intervals[idx][0] < inStart:
            res.append(intervals[idx])
        #判断最后插入的数据是否可以与前半部分集合
        if not res or res[-1][-1] > inStart:
            res.append(newInterval)
        else:
            res[-1][1] = max(res[-1][1], inEnd)
        #合并后半部分
        while idx < n:
            start, end = intervals[idx]
            if res[-1][1] > start:
                res[-1][1] = max(res[-1][1], end)
            else:
                res.append(intervals[idx])
        return res
