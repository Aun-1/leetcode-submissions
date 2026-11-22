from collections import deque 
class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
    
        # def dfs(r, c):
        #     # Stop conditions
        #     if r < 0 or r >= rows or c < 0 or c >= cols:
        #         return                      # off the grid
        #     if image[r][c] != original:
        #         return                      # wrong color (or already painted)

        #     image[r][c] = color             # paint = mark visited

        #     dfs(r - 1, c)                   # up
        #     dfs(r + 1, c)                   # down
        #     dfs(r, c - 1)                   # left
        #     dfs(r, c + 1)                   # right

        # original = image[sr][sc]
        # if original == color:
        #     return image

        # rows, cols = len(image), len(image[0])

        # dfs(sr, sc)
        # return image


        rows = len(image)
        cols = len(image[0])

        visited = set()
        original = image[sr][sc]

        queue = deque([(sr, sc)])
        visited.add((sr, sc))


        while queue:
            r, c = queue.popleft()
            image[r][c]=color
            for r_change, c_change in [(1,0),(-1,0),(0,1),(0,-1)]:
                next_r, next_c = r + r_change, c + c_change
                if(0<=next_r<rows and 0<=next_c<cols and image[next_r][next_c]==original and (next_r,next_c) not in visited):
                    visited.add((next_r,next_c))
                    queue.append((next_r,next_c))


        return image