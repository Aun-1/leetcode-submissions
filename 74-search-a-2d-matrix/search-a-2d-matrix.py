class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        # --- Search 1: find the row ---
        # CONDITION: row mid could still hold target (its last element is >= target)
        lo, hi = 0, m
        while lo < hi:
            mid = (lo + hi) // 2
            if matrix[mid][-1] >= target:
                hi = mid          # candidate -> shrink right
            else:
                lo = mid + 1       # ruled out -> shrink left
        row = lo

        # RULE: sentinel check — row could be m (target bigger than everything),
        # and the next lines index matrix[row], so we must guard first
        if row == m:
            return False

        # --- Search 2: find the column within that row ---
        # CONDITION: matrix[row][mid] could still be target
        lo, hi = 0, n
        while lo < hi:
            mid = (lo + hi) // 2
            if matrix[row][mid] >= target:
                hi = mid          # candidate -> shrink right
            else:
                lo = mid + 1       # ruled out -> shrink left

        # RULE: sentinel check — lo could be n (target bigger than everything in this row),
        # and the next line indexes matrix[row][lo]
        if lo == n:
            return False

        return matrix[row][lo] == target