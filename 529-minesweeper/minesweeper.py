class Solution:
    def updateBoard(self, board: list[list[str]], click: list[int]) -> list[list[str]]:
        r, c = click

        # Rule 1: clicked a mine, game over
        if board[r][c] == 'M':
            board[r][c] = 'X'
            return board

        rows, cols = len(board), len(board[0])

        # All 8 neighbors: 4 sides + 4 diagonals
        dirs = [(-1, -1), (-1, 0), (-1, 1),
                (0, -1),           (0, 1),
                (1, -1),  (1, 0),  (1, 1)]

        def dfs(r, c):
            # Stop conditions
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return                          # off the board
            if board[r][c] != 'E':
                return                          # already revealed (or a mine)

            # Count mines around this square
            mines = 0
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == 'M':
                    mines += 1

            # Rule 3: touching a mine, show the number and STOP
            if mines > 0:
                board[r][c] = str(mines)
                return

            # Rule 2: no mines nearby, mark blank and spread
            board[r][c] = 'B'
            for dr, dc in dirs:
                dfs(r + dr, c + dc)

        dfs(r, c)
        return board