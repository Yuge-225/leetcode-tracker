import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def calculate_dist(point):
            return point[0] * point[0] + point[1] * point[1]

        heap = []
        for point in points:

            distance = calculate_dist(point)
            heapq.heappush(heap,(-distance,point))
            if len(heap) > k:
                heapq.heappop(heap)

        return [point for _,point in heap]



        