class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i, j = 0, len(matrix) - 1
        row = -1
        while i <= j:
            mid = i + (j - i) // 2
            if matrix[mid][0] <= target:
                i = mid + 1
            else:
                j = mid - 1

        row = j
        
        i, j = 0, len(matrix[row]) - 1
        col = -1
        while i <= j:
            mid = i + (j - i) // 2
            if matrix[row][mid] == target:
                col = mid
                break
            elif matrix[row][mid] > target:
                j = mid - 1
            else:
                i = mid + 1
        
        if col == -1:
            return False

        return True