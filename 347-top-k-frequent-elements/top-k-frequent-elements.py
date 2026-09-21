import heapq
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        heap = []
        dicti = {}
        for x in nums:
            dicti[x] = dicti.get(x,0) + 1
        print(dicti)
        for x in dicti:

            heapq.heappush(heap,(dicti[x],x))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        print(f"heap = {heap}")
        for freq,x in heap:
            res.append(x)
        return res
