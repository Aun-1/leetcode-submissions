from collections import deque 

class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        # def DFS(r,c):
        #     if r < 0 or r >= m or c < 0 or c >= n:
        #         return 
        #     if board[r][c]=="X" or board[r][c]=="U":
        #         return 
        #     board[r][c]="U"
        #     DFS(r+1,c)
        #     DFS(r-1,c)
        #     DFS(r,c+1)
        #     DFS(r,c-1)
        visited=set()
        def bfs(start_row, start_col):
            queue = deque([(start_row, start_col)])
            while queue:
                r, c = queue.popleft()
                visited.add((start_row, start_col))
                board[r][c]="U"
                for r_change, c_change in [(1,0),(-1,0),(0,1),(0,-1)]:
                    next_r, next_c = r + r_change, c + c_change
                    if(0<=next_r<m and 0<=next_c<n and board[next_r][next_c]=="O" and (next_r,next_c) not in visited):
                        visited.add((next_r,next_c))
                        queue.append((next_r,next_c))
            
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                    if  board[i][j]=="O":
                        board[i][j]="U"
                        bfs(i,j)
        
        for i in range(m):
            for j in range(n):
                if board[i][j]=="O":
                    board[i][j]="X"
                elif board[i][j]=="U":
                    board[i][j]="O"
                    