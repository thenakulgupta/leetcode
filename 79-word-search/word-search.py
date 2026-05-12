class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def isValidIdx(board, row, col):
            return not (row < 0 or row >= len(board) or col < 0 or col >= len(board[row]))
        def existHelper(board, row, col, word, i = 0):
            moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]

            if board[row][col] != word[i]:
                return False

            if i == len(word)-1:
                return True

            board[row][col] = "."

            for move in moves:
                rowMove, colMove = move
                newRow = row + rowMove
                newCol = col + colMove
                if isValidIdx(board, newRow, newCol) and board[newRow][newCol] != ".":
                    if existHelper(board, newRow, newCol, word, i + 1):
                        return True
            board[row][col] = word[i]
            return False


        for row in range(len(board)):
            for col in range(len(board[row])):
                if existHelper(board, row, col, word):
                    return True

        return False