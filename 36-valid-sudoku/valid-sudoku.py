class Solution(object):
    def checkIsValidNumber(self, board, i, j, number):
        sqRowNumber = (i // 3) * 3
        sqColNumber = (j // 3) * 3

        for n in range(9):
            if board[i][n] == number and n != j:
                return False
            if board[n][j] == number and n != i:
                return False

        for m in range(3):
            for n in range(3):
                if (sqRowNumber + m != i or sqColNumber + n != j) and board[sqRowNumber + m][sqColNumber + n] == number:
                    return False
        return True

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            for j in range(9):
                k = board[i][j]
                if k != ".":
                    num = str(k)
                    if not self.checkIsValidNumber(board, i, j, num):
                        return False
        return True