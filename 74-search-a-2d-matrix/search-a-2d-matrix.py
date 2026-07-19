class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        lo, hi = 0, m
        while lo < hi:
            mid = (hi + lo) // 2
            if matrix[mid][-1] < target:
                lo = mid + 1   # ruled out -> shrink left
            else:
                hi = mid         # candidate -> shrink right
        row = lo

        if row == m:
            return False

        lo, hi = 0, n -1
        while lo < hi:
            mid = (hi + lo) // 2
            if matrix[row][mid] < target:
                lo = mid + 1   # ruled out -> shrink left
            else:
                hi = mid      # candidate -> shrink right

        if lo == n:
            return False

        return matrix[row][lo] == target