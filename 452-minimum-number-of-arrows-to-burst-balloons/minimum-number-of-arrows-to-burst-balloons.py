class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key=lambda x:x[1])
        arrows_used = 1
        prev_end = points[0][1]
        for point in points:
            if point[0] > prev_end:
                prev_end = point[1]
                arrows_used += 1
            else:
                continue
        return arrows_used
