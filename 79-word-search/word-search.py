class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def existHelper(board, row, col, word, visited, i = 0):
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[row]):
                return False

            if i >= len(word):
                return False

            moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]

            if board[row][col] != word[i]:
                return False

            if i == len(word)-1:
                return True

            visited.add((row, col))

            for move in moves:
                rowMove, colMove = move
                newRow = row + rowMove
                newCol = col + colMove
                if (newRow, newCol) not in visited:
                    if existHelper(board, newRow, newCol, word, visited, i + 1):
                        return True
            visited.discard((row, col))
            return False


        for row in range(len(board)):
            for col in range(len(board[row])):
                if existHelper(board, row, col, word, set()):
                    return True

        return False