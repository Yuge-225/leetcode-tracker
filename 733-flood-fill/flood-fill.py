class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        visited = set()
        source_color = image[sr][sc]
        self.dfs(image,sr,sc,visited,source_color,color)
        return image
    
    def dfs(self,image,i,j,visited,source_color,color):

        if i < 0 or i >= len(image):
            return
        if j < 0 or j >= len(image[0]):
            return
        if (i,j) in visited:
            return
        if image[i][j] != source_color:
            return

        visited.add((i,j))
        image[i][j] = color

        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        for dx,dy in directions:
            self.dfs(image,dx+i,dy+j,visited,source_color,color)



