class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x:x[0])
        res = []
        for interval in intervals:
            if not res:
                res.append(interval)
            elif res[-1][1] < interval[0]: # 当前正在构建集合的尾部 和 即将加入的interval首部不连接
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res