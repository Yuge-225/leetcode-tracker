import heapq
from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        dist = [float("inf")] * n
        dist[src] = 0
        for _ in range(k+1):
            new_dist = dist.copy()
            for u,v,w in flights:
                if dist[u] != float("inf") and dist[u] + w < new_dist[v]:
                    new_dist[v] = dist[u] + w
            dist = new_dist
        return dist[dst] if dist[dst] != float("inf") else -1 