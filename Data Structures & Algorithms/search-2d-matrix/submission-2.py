class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        if target < matrix[0][0] or target > matrix[m - 1][n - 1]:
            return False
        
        left, right = 0, m - 1
        foundRow = None
        while left <= right:
            mid = left + ((right - left) // 2)
            if target >= matrix[mid][0] and target <= matrix[mid][n - 1]:
                foundRow = mid
                break
            if target > matrix[mid][n - 1]:
                left = mid + 1
            else:
                right = mid - 1
        if foundRow is None:
            return False

        left, right = 0, n - 1
        while left <= right:
            mid = left + ((right - left) // 2)
            if target == matrix[foundRow][mid]:
                return True
            elif target > matrix[foundRow][mid]:
                left = mid + 1
            else:
                right = mid - 1
        return False