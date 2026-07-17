class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        def dfs(grid,i,j,visited):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return
            if (i,j) in visited:
                return
            
            visited.add((i,j))    
            directions = [(-1,0),(1,0),(0,1),(0,-1)]


            for dx, dy in directions:
                new_i = i + dx
                new_j = j + dy
                
                if new_i < 0 or new_i >= len(grid) or new_j < 0 or new_j >= len(grid[0]):
                    continue
                
                if grid[new_i][new_j] < grid[i][j]:
                    continue

                dfs(grid,new_i,new_j,visited)
        
        grid = heights
        pacific_visited = set()
        atlantic_visited = set()
        
        # grid上边
        for j in range(len(grid[0])):
            dfs(grid,0,j,pacific_visited)
        
        # grid 左边
        for i in range(len(grid)):
            dfs(grid,i,0,pacific_visited)
        
        # grid 下边
        for j in range(len(grid[0])):
            dfs(grid,len(grid)-1, j, atlantic_visited)

        # grid 右边
        for i in range(len(grid)):
            dfs(grid,i,len(grid[0])-1,atlantic_visited)

        res = []
        for points in atlantic_visited:
            if points in pacific_visited:
                res.append(points)
        return res
