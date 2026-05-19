class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        protectedOBoxes = set()
        m, n = len(board), len(board[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def protectBoxes(board, i, j):
            protectedOBoxes.add((i, j))
            for r, c in dirs:
                newR = i + r
                newC = j + c
                if (newR < 0 or newC < 0 or
                    newR > m - 1 or newC > n - 1 or
                    (newR, newC) in protectedOBoxes or
                    board[newR][newC] == 'X'):
                    continue
                protectBoxes(board, newR, newC)
        
        for i in range(m):
            if board[i][0] == 'X':
                continue
            protectBoxes(board, i, 0)
        
        for i in range(n):
            if board[0][i] == 'X':
                continue
            protectBoxes(board, 0, i)

        for i in range(m):
            if board[i][n - 1] == 'X':
                continue
            protectBoxes(board, i, n - 1)

        for i in range(n):
            if board[m - 1][i] == 'X':
                continue
            protectBoxes(board, m - 1, i)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and (i, j) not in protectedOBoxes:
                    board[i][j] = 'X'