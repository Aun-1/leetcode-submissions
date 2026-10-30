class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        def findRow(matrix, target):
            left = 0
            right = len(matrix)-1

            while left <= right:
                mid = (left + right) //2
                if matrix[mid][0] < target:
                    left = mid + 1
                elif matrix[mid][0] == target:
                    return mid 
                else:
                    right = mid - 1
            return right
                
        
        row = findRow(matrix, target)
        left = 0
        right = len(matrix[row])-1

        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False
        