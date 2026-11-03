class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        def DFS(r,c):
            if r < 0 or r >= m or c < 0 or c >= n:
                return 
            if board[r][c]=="X" or board[r][c]=="U":
                return 
            board[r][c]="U"
            DFS(r+1,c)
            DFS(r-1,c)
            DFS(r,c+1)
            DFS(r,c-1)
            
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                    if  board[i][j]=="O":
                        DFS(i,j)
        
        for i in range(m):
            for j in range(n):
                if board[i][j]=="O":
                    board[i][j]="X"
                elif board[i][j]=="U":
                    board[i][j]="O"
                    