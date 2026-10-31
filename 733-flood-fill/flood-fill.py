class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
    
        def dfs(r, c):
            # Stop conditions
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return                      # off the grid
            if image[r][c] != original:
                return                      # wrong color (or already painted)

            image[r][c] = color             # paint = mark visited

            dfs(r - 1, c)                   # up
            dfs(r + 1, c)                   # down
            dfs(r, c - 1)                   # left
            dfs(r, c + 1)                   # right

        original = image[sr][sc]
        if original == color:
            return image

        rows, cols = len(image), len(image[0])

        dfs(sr, sc)
        return image