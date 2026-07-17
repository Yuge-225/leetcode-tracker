class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        safe_o = set()

        def dfs(grid, i, j, safe_o):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return 
            if (i,j) in safe_o:
                return
            
            safe_o.add((i,j))

            directions = [(-1,0),(1,0),(0,-1),(0,1)]
            for dx, dy in directions:
                new_i = i + dx
                new_j = j + dy
                
                if new_i < 0 or new_i >= len(grid) or new_j < 0 or new_j >= len(grid[0]):
                    continue
                if grid[new_i][new_j] == 'X':
                    continue
                dfs(grid,new_i,new_j,safe_o)
        
        row = len(board)
        col = len(board[0])
        # 上边
        for j in range(col):
            if board[0][j] == 'O':
                dfs(board,0,j,safe_o)
            else:
                continue
        
        # 左边
        for i in range(row):
            if board[i][0] == 'O':
                dfs(board,i,0,safe_o)
        
        # 下边
        for j in range(col):
            if board[row-1][j] == 'O':
                dfs(board,row-1,j,safe_o)
        
        # 右边
        for i in range(row):
            if board[i][col-1] == 'O':
                dfs(board,i,col-1,safe_o)
        
        for i in range(row):
            for j in range(col):
                if (i,j) not in safe_o and board[i][j] == 'O':
                    board[i][j] = 'X'

                