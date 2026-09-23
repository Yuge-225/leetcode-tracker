import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        dest_to = [float("inf")] * n
        start = k-1
        dest_to[start] = 0
        pq = [(0,start)]
        graph = defaultdict(list)

        for each_pair in times:
            source = each_pair[0] - 1
            dest = each_pair[1] - 1
            weight = each_pair[2]
            graph[source].append((dest,weight))

        while pq:
            dist,cur = heapq.heappop(pq)
            if dist > dest_to[cur]:
                continue
            for neighbor,weight in graph[cur]:
                new_dist = dest_to[cur] + weight
                if new_dist < dest_to[neighbor]:
                    dest_to[neighbor] = new_dist
                    pq.append((new_dist,neighbor))
        return max(dest_to) if max(dest_to) != float("inf") else -1
        
                