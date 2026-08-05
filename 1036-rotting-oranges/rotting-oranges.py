from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = set()
        queue = deque()
        fresh_count = 0
        # 先找到所有腐烂橘子
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    visited.add((i,j))
                    queue.append((i,j))
                if grid[i][j] == 1:
                    fresh_count += 1
        if fresh_count == 0:
            return 0
        
        time = 0
        while queue and fresh_count > 0:
            sz = len(queue)
            for _ in range(sz):
                node = queue.popleft()
                directions = [(-1,0),(1,0),(0,-1),(0,1)]

                for dx,dy in directions:
                    new_x = node[0] + dx
                    new_y = node[1] + dy
                    if new_x >= m or new_x < 0 or new_y >= n or new_y < 0:
                        continue
                    if (new_x,new_y) not in visited and grid[new_x][new_y] == 1:

                        visited.add((new_x,new_y))
                        queue.append((new_x,new_y))
                        fresh_count -= 1
            time += 1
        
        return time if fresh_count == 0 else -1














"""

from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        # 初始化，找到所有的rotten作为起点，统计fresh的数量
        visited = set()
        queue = deque()
        fresh_count = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    visited.add((i,j))
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    fresh_count += 1
        
        if fresh_count == 0:
            return 0
        
        # BFS: 只要还有新鲜橘子，并且队列不为空，就继续扩散
        step = 0
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        while queue and fresh_count > 0:
            sz = len(queue)
            for _ in range(sz):
                x, y = queue.popleft()

                for dx, dy in directions:
                    new_x, new_y = x + dx, y + dy
                    neighbor = (new_x, new_y)

                    if new_x < 0 or new_x >= rows or new_y < 0 or new_y >= cols:
                        continue
                    if grid[new_x][new_y] != 1:
                        continue
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
                        fresh_count -= 1
            step += 1
        return step if fresh_count == 0 else -1
"""