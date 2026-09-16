class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        intervals.append(newInterval)
        intervals.sort(key = lambda x:x[0])
        res = []
        for interval in intervals:
            if not res:
                res.append(interval)
            elif res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1],interval[1])
        return res