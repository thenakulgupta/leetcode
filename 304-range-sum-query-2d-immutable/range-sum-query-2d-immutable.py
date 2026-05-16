class NumMatrix:

    def getSafeValue(self, row, col):
        matrix = self.matrix
        return 0 if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]) else matrix[row][col]

    def __init__(self, matrix: List[List[int]]):
        self.matrix = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]

        for row in range(1, len(self.matrix)):
            for col in range(1, len(self.matrix[0])):
                self.matrix[row][col] = matrix[row - 1][col - 1] + self.getSafeValue(row - 1, col) + self.getSafeValue(row, col - 1) - self.getSafeValue(row - 1, col - 1)


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.getSafeValue(row2 + 1, col2 + 1) - self.getSafeValue(row1, col2 + 1) - self.getSafeValue(row2 + 1, col1) + self.getSafeValue(row1, col1)



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)