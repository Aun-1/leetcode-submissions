class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        queue = deque([(0, 0)])
        visited = {(0, 0)}
        steps = 1                                          # ← CHANGES: 1 if the start counts, else 0
        while queue:
            for _ in range(len(queue)):                    # one ring = one step
                row, col = queue.popleft()
                if row == n - 1 and col == n - 1:          # ← CHANGES: goal check
                    return steps
                for row_change in (-1, 0, 1):              # ← CHANGES: 8 directions here
                    for col_change in (-1, 0, 1):
                        next_row, next_col = row + row_change, col + col_change
                        if (0 <= next_row < n and 0 <= next_col < n
                                and grid[next_row][next_col] == 0
                                and (next_row, next_col) not in visited):
                            visited.add((next_row, next_col))
                            queue.append((next_row, next_col))
            steps += 1
        return -1