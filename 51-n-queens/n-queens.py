class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["." for _ in range(n)] for _ in range(n)]
        self.finalBoard = []

        def isValidPosition(board, i, j, colSet, diag1Set, diag2Set):
            if j in colSet:
                return False

            if j + i in diag1Set:
                return False

            if i - j in diag2Set:
                return False

            return True


        def nQueens(board, i, colSet, diag1Set, diag2Set):
            if i == n:
                self.finalBoard.append(["".join(_) for _ in board])
                return True
            
            for j in range(n):
                if isValidPosition(board, i, j, colSet, diag1Set, diag2Set):
                    board[i][j] = 'Q'
                    colSet.add(j)
                    diag1Set.add(j + i)
                    diag2Set.add(i - j)
                    nQueens(board, i + 1, colSet, diag1Set, diag2Set)
                    board[i][j] = '.'
                    colSet.remove(j)
                    diag1Set.remove(j + i)
                    diag2Set.remove(i - j)

            return False


        nQueens(board, 0, set(), set(), set())
        return self.finalBoard