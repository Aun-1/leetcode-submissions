class Solution:
    def countBattleships(self, board: list[list[str]]) -> int:
        m = len(board)
        n = len(board[0])


        visited = []
        for _ in range(m):
            visited.append([False]*n)
        
        ships = 0

        def DFS(row, column):
            if row<0 or row>=m or column < 0 or column >= n:
                return 
            if board[row][column] != 'X' or visited[row][column]==True:
                return 
            board[row][column] = True
            DFS(row + 1, column)
            DFS(row -1, column)
            DFS(row, column + 1)
            DFS(row, column - 1)

        
        for row in range(m):
            for column in range(n):
                if board[row][column] == "X" and not visited[row][column]:
                    ships += 1
                    DFS(row, column)
        
        return ships
                
        
        
