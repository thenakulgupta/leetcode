class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.ans = 0
        self.visited = set()
        self.graph = deque()

        def isSafe(grid, i, j):
            return not (i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]))
            
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    self.visited.add((i, j))
                    self.graph.append((i, j, 0))

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while len(self.graph):
            i1, j1, k = self.graph.popleft()
            self.ans = max(self.ans, k)
            for _dir in dirs:
                i2, j2 = _dir
                newI = i1 + i2
                newJ = j1 + j2
                if isSafe(grid, newI, newJ) and grid[newI][newJ] == 1 and (newI, newJ) not in self.visited:
                    self.visited.add((newI, newJ))
                    self.graph.append((newI, newJ, k + 1))
                    grid[newI][newJ] = 2

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    return -1

        return self.ans