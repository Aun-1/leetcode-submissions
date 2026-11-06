from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        queue = deque()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh+=1
                elif grid[r][c] == 2:
                    queue.append((r,c))

        minutes = 0
        while queue and fresh > 0:
            for _ in range(len(queue)):
                row, col = queue.popleft()

                for row_change, col_change in ((-1,0),(1,0),(0,-1),(0,1)):
                    next_row, next_col = row + row_change, col + col_change
                    if(0<=next_row<rows and 0<=next_col<cols and grid[next_row][next_col]==1):
                        grid[next_row][next_col] = 2
                        fresh -= 1
                        queue.append((next_row, next_col))

            minutes+=1

        if fresh == 0:
            return minutes
        else:
            return -1