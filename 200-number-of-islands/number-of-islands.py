class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.visited = set()
        self.graph = deque()
        self.ans = 0

        def isSafe(grid, i, j):
            return not (i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]))

        def bfs(grid, i, j):
            if grid[i][j] != '1':
                return

            if (i, j) in self.visited:
                return

            self.visited.add((i, j))
            self.graph.append((i, j))
            dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            while len(self.graph):
                i1, j1 = self.graph.popleft()
                for _dir in dirs:
                    i2, j2 = _dir
                    newI = i1 + i2
                    newJ = j1 + j2
                    if isSafe(grid, newI, newJ) and (newI, newJ) not in self.visited and grid[newI][newJ] == '1':
                        self.graph.append((newI, newJ))
                        self.visited.add((newI, newJ))

            self.ans += 1


        for i in range(len(grid)):
            for j in range(len(grid[i])):
                bfs(grid, i, j)
        
        return self.ans