from collections import deque
class Solution:
    def maxDistance(self, grid: list[list[int]]) -> int:
        
        n = len(grid)
        queue = deque()
        water = 0

        for r in range(n):
            for c in range(n):
                if grid[r][c]==1:
                    queue.append((r,c))
                else:
                    water+=1
        
        if water == 0 or len(queue)==0:
            return -1

        steps = 0
        while queue and water > 0:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for row_change, col_change in ((-1,0),(1,0),(0,-1),(0,1)):
                    next_row, next_col = row + row_change, col + col_change
                    if 0 <= next_row < n and 0 <= next_col < n and grid[next_row][next_col]==0:
                        grid[next_row][next_col] = 1
                        water -= 1
                        queue.append((next_row, next_col))
            steps+=1
        
        return steps