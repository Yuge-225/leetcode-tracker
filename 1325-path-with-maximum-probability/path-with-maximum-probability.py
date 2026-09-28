import heapq
from collections import defaultdict
class Solution:
    def maxProbability(self, n: int, edges: list[list[int]], succProb: list[float], start_node: int, end_node: int) -> float:
        prob_to = [0] * n
        prob_to[start_node] =  1
        pq = [(-1,start_node)]

        graph = defaultdict(list)
        for i in range(len(edges)):
            a,b = edges[i][0],edges[i][1]
            weight = succProb[i]
            graph[a].append((b,weight))
            graph[b].append((a,weight))

        while pq:
            neg_prob, cur = heapq.heappop(pq)
            prob = -neg_prob
            if prob < prob_to[cur]:
                continue
            for neighbor,weight in graph[cur]:
                new_prob = weight * prob_to[cur]
                if new_prob > prob_to[neighbor]:
                    prob_to[neighbor] = new_prob
                    heapq.heappush(pq,(-new_prob,neighbor))
        
        return prob_to[end_node]
            
            
