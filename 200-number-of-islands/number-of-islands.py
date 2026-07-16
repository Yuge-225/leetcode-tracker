class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i,j) not in visited:
                    count += 1
                    self.dfs(grid,i,j,visited)
        return count

    def dfs(self,grid,i,j,visited):
        if i < 0 or i >= len(grid):
            return
        if j < 0 or j >= len(grid[0]):
            return
            
        if grid[i][j] == '0':
            return
            
        if (i,j) in visited:
            return
            
        visited.add((i,j))
            
        directions = [
                (-1,0),
                (1,0),
                (0,-1),
                (0,1)
        ]
        for dx,dy in directions:
            self.dfs(grid,i+dx,j+dy,visited)
            