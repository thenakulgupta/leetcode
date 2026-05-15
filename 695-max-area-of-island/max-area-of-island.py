class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.ans = 0
        self.visited = set()

        def isSafe(grid, i, j):
            return not (i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]))

        def dfs(grid, i, j):
            if not isSafe(grid, i, j):
                return

            if grid[i][j] != 1:
                return

            if (i, j) in self.visited:
                return

            self.visited.add((i, j))

            dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            self._len += 1

            for _dir in dirs:
                i2, j2 = _dir
                newI = i + i2
                newJ = j + j2
                dfs(grid, newI, newJ)


        for i in range(len(grid)):
            for j in range(len(grid[i])):
                self._len = 0
                dfs(grid, i, j)
                self.ans = max(self.ans, self._len)

        return self.ans