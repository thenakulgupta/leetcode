class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        protectedOBoxes = set()
        m, n = len(board), len(board[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def protectBoxes(board, i, j):
            if i < 0 or j < 0 or i > m - 1 or j > n - 1:
                return
            if (i, j) in protectedOBoxes:
                return
            if board[i][j] == 'X':
                return
            protectedOBoxes.add((i, j))
            for r, c in dirs:
                newR = i + r
                newC = j + c
                protectBoxes(board, newR, newC)
        
        for i in range(m):
            protectBoxes(board, i, 0)
            protectBoxes(board, i, n - 1)
        
        for i in range(n):
            protectBoxes(board, 0, i)
            protectBoxes(board, m - 1, i)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and (i, j) not in protectedOBoxes:
                    board[i][j] = 'X'