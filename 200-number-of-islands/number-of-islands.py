class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.visited = set()
        self.ans = 0

        def isSafe(grid, i, j):
            return not (i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]))

        def dfs(grid, i, j, isFirst = True):
            if not isSafe(grid, i, j):
                return

            if grid[i][j] != '1':
                return

            if (i, j) in self.visited:
                return

            self.visited.add((i, j))
            dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            if isFirst:
                self.ans += 1
                isFirst = False
            for _dir in dirs:
                i2, j2 = _dir
                newI = i + i2
                newJ = j + j2
                dfs(grid, newI, newJ, isFirst)


        for i in range(len(grid)):
            for j in range(len(grid[i])):
                dfs(grid, i, j)
        
        return self.ans