class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        count = 0
        prev_end = float('-inf')
        for interval in intervals:
            if interval[0] >= prev_end: # 当前会议的起始时间等于或者晚于上一个会议结束时间
                prev_end = interval[1]
            else:
                count += 1
        return count