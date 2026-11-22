class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        n = len(maze)
        m = len(maze[0])
        queue = deque([(entrance[0], entrance[1])])
        visited = {(entrance[0], entrance[1])}
        steps = 0                                          # ← CHANGES: 1 if the start counts, else 0
        while queue:
            for _ in range(len(queue)):                    # one ring = one step
                row, col = queue.popleft()
                if (row == n - 1 or col == m - 1 or row == 0 or col==0) and [row, col]!= entrance:          # ← CHANGES: goal check
                    return steps
                for row_change, col_change in [(1,0), (-1,0), (0,1), (0,-1)]:
                        next_row, next_col = row + row_change, col + col_change
                        if (0 <= next_row < n and 0 <= next_col < m
                                and maze[next_row][next_col] == "."
                                and (next_row, next_col) not in visited):
                            visited.add((next_row, next_col))
                            queue.append((next_row, next_col))
            steps += 1
        return -1