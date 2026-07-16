class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        visited = set()
        max_area = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i,j) not in visited:
                    curr_area = self.dfs(grid,i,j,visited)
                    max_area = max(max_area,curr_area)
                
        return max_area
    
    def dfs(self,grid,i,j,visited):
        if i < 0 or i >= len(grid):
            return 0
        if j < 0 or j >= len(grid[0]):
            return 0 
        if grid[i][j] == 0:
            return 0
        if (i,j) in visited:
            return 0
        
        visited.add((i,j))
        curr_area = 1

        directions = [
            (-1,0),
            (1,0),
            (0,-1),
            (0,1)
        ]
        
        for dx,dy in directions:
            curr_area += self.dfs(grid,i+dx,j+dy,visited)
        
        return curr_area
        

