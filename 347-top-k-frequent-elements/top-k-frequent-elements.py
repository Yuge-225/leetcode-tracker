import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for x in nums:
            count[x] = count.get(x,0) + 1
        heap = []
        for key in count:
            heapq.heappush(heap,(count[key],key))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for each_pair in heap:
            key = each_pair[1]
            res.append(key)
        return res
            


        