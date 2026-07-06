import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def calculate_dist(point):
            return point[0] * point[0] + point[1] * point[1]

        heap = []
        for point in points:

            distance = calculate_dist(point)
            print(f"point = {point}, distance = {distance}")
            heapq.heappush(heap,(-distance,point))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for candidate in heap:
            res.append(candidate[1])
        return res



        