class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        visited = []
        for _ in range(len(grid)):
            visited.append([False] * len(grid[0]))
        
        rows= len(grid)
        cols=len(grid[0])

        def DFS(row, col):
            if row<0 or row>=rows or col < 0 or col >= cols:
                return 0
            if grid[row][col]!=1 or visited[row][col]==True:
                return 0
            visited[row][col]=True
            return (1+DFS(row+1, col) +DFS(row-1, col) + DFS(row, col+1) + DFS(row, col-1))

        maxA=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1 and not visited[i][j]:
                    maxA=max(DFS(i,j), maxA)
        return maxA
        
