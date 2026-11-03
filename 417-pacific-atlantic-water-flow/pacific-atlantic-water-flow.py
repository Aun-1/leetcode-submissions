class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        m, n = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        def DFS(r, c, value, visited):
            if r < 0 or r >= m or c < 0 or c >= n:
                return
            if (r, c) in visited or heights[r][c] < value:
                return
            visited.add((r, c))
            value = heights[r][c]
            DFS(r + 1, c, value, visited)
            DFS(r - 1, c, value, visited)
            DFS(r, c + 1, value, visited)
            DFS(r, c - 1, value, visited)

        for r in range(m):
            DFS(r, 0, 0, pacific)        # left column
            DFS(r, n - 1, 0, atlantic)   # right column
        for c in range(n):
            DFS(0, c, 0, pacific)        # top row
            DFS(m - 1, c, 0, atlantic)   # bottom row

        result = []
        for r in range(m):
            for c in range(n):
                if (r, c) in pacific and (r, c) in atlantic:
                    result.append([r, c])
        return result