class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        def DFS(r,c):
            if r < 0 or r >= m or c < 0 or c >= n:
                return 
            if grid[r][c] == 1 or grid[r][c] == -1:
                return 
            grid[r][c]=-1
            DFS(r+1,c)
            DFS(r-1,c)
            DFS(r,c+1)
            DFS(r,c-1)
        

        for i in range(m):
            DFS(i,0)
            DFS(i,n-1)
        for j in range(n):
            DFS(0,j)
            DFS(m-1,j)
        
        island = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    island+=1
                    DFS(i,j)
        
        return island
