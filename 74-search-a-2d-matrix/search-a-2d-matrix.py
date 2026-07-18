class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        while i < len(matrix):
            if matrix[i][-1] < target:
                i += 1
            else:
                break
        if i == len(matrix):
            return False   # target bigger than everything

        lo = 0
        hi = len(matrix[i]) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if matrix[i][mid] > target:
                hi = mid - 1
            elif matrix[i][mid] < target:
                lo = mid + 1
            else:
                return True
        return False