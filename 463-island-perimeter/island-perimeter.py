'''
solution that coems ot midn first is dfs
--> call by using 2 i and j for loops and soo as the fist block is foudn call dfs and stop loop

--> each call is returned with 0 if it is off grid or water
--> each cell is checks 0 or out of coubary on all 4 cornets and total and returns total + next dfs calls 

'''
class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        
        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols or grid[r][c]!=1:
                return 0
            
            grid[r][c]=2

            total = 0
            if r-1<0:
                total+=1
            elif grid[r-1][c]==0:
                total+=1
            if r+1>=rows:
                total+=1
            elif grid[r+1][c]==0:
                total+=1
            if c-1<0:
                total+=1
            elif grid[r][c-1]==0:
                total+=1
            if c+1>=cols:
                total+=1
            elif grid[r][c+1]==0:
                total+=1
            return total + dfs(r+1,c)+dfs(r-1,c)+dfs(r,c+1)+dfs(r,c-1)

        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    return dfs(i,j)