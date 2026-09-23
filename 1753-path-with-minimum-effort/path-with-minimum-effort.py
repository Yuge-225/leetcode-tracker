import heapq
class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        dest_to = [[float("inf")] * cols for _ in range(rows)]
        dest_to[0][0] = 0
        pq = [(0,(0,0))]

        while pq:
            dist,points = heapq.heappop(pq)
            x,y = points[0],points[1]

            if dist > dest_to[x][y]:
                continue
            
            directions = [(-1,0),(1,0),(0,1),(0,-1)]
            for dx, dy in directions:
                nx = x+dx
                ny = y+dy

                if 0 <= nx < rows and 0 <= ny < cols:
                    edge_weight = abs(heights[nx][ny] - heights[x][y])
                    candidate_dist = max(dist,edge_weight)
                    if candidate_dist < dest_to[nx][ny]:
                        dest_to[nx][ny] = candidate_dist
                        heapq.heappush(pq,(candidate_dist,(nx,ny)))
        return dest_to[rows-1][cols-1]
        