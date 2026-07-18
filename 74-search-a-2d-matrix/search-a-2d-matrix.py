class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        lo, hi = 0, m - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if matrix[mid][-1] >= target:
                hi = mid
            else:
                lo = mid + 1
        row = lo

        lo, hi = 0, n - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if matrix[row][mid] >= target:
                hi = mid
            else:
                lo = mid + 1

        return matrix[row][lo] == target