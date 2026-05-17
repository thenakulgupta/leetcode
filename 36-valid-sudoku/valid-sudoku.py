class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isValid(board, i, j):
            if board[i][j] == ".":
                return True
            boxRow, boxCol = (i // 3) * 3, (j // 3) * 3
            for k in range(9):
                if i != k and board[k][j] == board[i][j]:
                    return False
                if j != k and board[i][k] == board[i][j]:
                    return False
                r, c = boxRow + k // 3, boxCol + k % 3
                if not (i == r and j == c) and board[r][c] == board[i][j]:
                    return False
            return True

        for i in range(9):
            for j in range(9):
                if not isValid(board, i, j):
                    return False
        return True