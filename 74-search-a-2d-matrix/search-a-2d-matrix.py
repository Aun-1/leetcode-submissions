class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix) 
        lo, hi = 0, m
        while lo < hi:
            mid = (lo + hi) // 2
            if matrix[mid][-1] >= target:
                hi = mid          # candidate -> shrink right
            else:
                lo = mid + 1       # ruled out -> shrink left
        row = lo

        if row == m:
            return False

        n=len(matrix[0])
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