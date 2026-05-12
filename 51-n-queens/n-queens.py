class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["." for _ in range(n)] for _ in range(n)]
        self.finalBoard = []

        def isValidPosition(board, i, j):
            n = len(board)
            for row in range(n):
                if i != row and board[row][j] == 'Q':
                    return False
            row, col = i - 1, j - 1
            while row >= 0 and col >= 0:
                if board[row][col] == 'Q':
                    return False
                row -= 1
                col -= 1
            row, col = i - 1, j + 1
            while row >= 0 and col < n:
                if board[row][col] == 'Q':
                    return False
                row -= 1
                col += 1
            row, col = i + 1, j - 1
            while row < n and col >= 0:
                if board[row][col] == 'Q':
                    return False
                row += 1
                col -= 1
            row, col = i + 1, j + 1
            while row < n and col < n:
                if board[row][col] == 'Q':
                    return False
                row += 1
                col += 1
            return True


        def nQueens(board, i = 0):
            if i == n:
                self.finalBoard.append(["".join(_) for _ in board])
                return True
            
            for j in range(n):
                if isValidPosition(board, i, j):
                    board[i][j] = 'Q'
                    nQueens(board, i + 1)
                    board[i][j] = '.'

            return False


        nQueens(board)
        return self.finalBoard