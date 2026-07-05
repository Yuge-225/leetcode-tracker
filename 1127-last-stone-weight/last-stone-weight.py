import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []

        for x in stones:
            heapq.heappush(max_heap,-x)
        
        while len(max_heap) > 1:
            y = -heapq.heappop(max_heap)
            x = -heapq.heappop(max_heap)
            if x == y:
                continue
            else:
                new_val = y - x
                heapq.heappush(max_heap,-new_val)
    
        return -heapq.heappop(max_heap) if max_heap else 0