from collections import deque
class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        rows = len(mat)
        cols = len(mat[0])
        visited=set()

        queue = deque()
        steps = 0

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append((r,c))
                    visited.add((r,c))

        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                mat[row][col] = steps

                for row_change, col_change in ((-1,0),(1,0),(0,-1),(0,1)):
                    next_row, next_col = row + row_change, col + col_change
                    if(0<=next_row<rows and 0<=next_col<cols and mat[next_row][next_col]==1 and (next_row, next_col) not in visited):
                        queue.append((next_row, next_col))
                        visited.add((next_row, next_col))

            steps+=1
        
        return mat






























        # rows = len(mat)
        # cols = len(mat[0])
        # visited=set()
        # queue = deque()

        # dist=[]
        # for _ in range(rows):
        #     dist.append([-1]*cols)
        
        # for i in range(rows):
        #     for j in range(cols):
        #         if mat[i][j]==0:
        #             dist[i][j]=0
        #             visited.add((i,j))
        #             queue.append((i,j))



        # while queue:
        #     for _ in range(len(queue)):
        #         row, col = queue.popleft()
        #         for row_change, col_change in ((-1,0),(1,0),(0,-1),(0,1)):
        #             next_row, next_col = row + row_change, col + col_change
        #             if (0 <= next_row < rows and 0 <= next_col < cols and dist[next_row][next_col] == -1 and (next_row, next_col) not in visited):
        #                 visited.add((next_row, next_col))
        #                 queue.append((next_row, next_col))
        #                 dist[next_row][next_col] = dist[row][col] + 1

        # return dist