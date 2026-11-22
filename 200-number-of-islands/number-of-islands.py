from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = set()
        island_c = 0

        def bfs(start_row, start_col):
            queue = deque([(start_row, start_col)])
            visited.add((start_row, start_col))

            while queue:
                r, c = queue.popleft()
                for r_change, c_change in [(1,0),(-1,0),(0,1),(0,-1)]:
                    next_r, next_c = r + r_change, c + c_change
                    if(0<=next_r<rows and 0<=next_c<cols and grid[next_r][next_c]=="1" and (next_r,next_c) not in visited):
                        visited.add((next_r,next_c))
                        queue.append((next_r,next_c))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    island_c +=1
                    bfs(row,col)

        return island_c