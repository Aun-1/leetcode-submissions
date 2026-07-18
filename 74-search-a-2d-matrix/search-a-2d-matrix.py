class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        # binary search to find the row
        lo, hi = 0, m - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                row = mid
                break
            elif matrix[mid][-1] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        else:
            return False

        # binary search within the row
        lo, hi = 0, n - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if matrix[row][mid] > target:
                hi = mid - 1
            elif matrix[row][mid] < target:
                lo = mid + 1
            else:
                return True
        return False