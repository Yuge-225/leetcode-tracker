import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for val in nums:
            heapq.heappush(heap,val)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]











"""

import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = []
        for val in nums:
            heapq.heappush(max_heap,-val)
        
        res = None
        while k > 0:
            top = -heapq.heappop(max_heap)
            k -= 1
            if k == 0:
                res = top
            
        return res




"""