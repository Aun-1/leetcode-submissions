class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:

        rows = len(board)
        cols = len(board[0])

        def dfs(r, c, index):                                   # CHANGED: index = position in word
            if index == len(word):                              # CHANGED: past the last letter → success
                return True
            if r<0 or c<0 or r>=rows or c>=cols or board[r][c] != word[index]:   # CHANGED: must be the NEXT letter
                return False
            letter = board[r][c]
            board[r][c]="0"

            found = dfs(r+1,c,index+1) or dfs(r-1,c,index+1) or dfs(r,c+1,index+1) or dfs(r,c-1,index+1)   # CHANGED: index+1

            board[r][c]=letter                                  # undo: restore the cell
            return found

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:                      # CHANGED: start only on the FIRST letter
                    if dfs(i,j,0):                              # CHANGED: begin at index 0
                        return True

        return False