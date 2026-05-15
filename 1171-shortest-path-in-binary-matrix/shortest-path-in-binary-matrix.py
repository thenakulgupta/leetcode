class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if len(grid) == 1 and grid[0][0] == 0:
            return 1
        if grid[0][0] != 0:
            return -1
        visited = set()
        visited.add((0,0))
        graph = deque([(0,0,-1)])
        ans = -1
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)]

        def isSafe(grid, i, j):
            return not (i < 0 or j < 0 or i >= len(grid) or j >= len(grid))

        while len(graph):
            i, j, k = graph.popleft()
            if i == len(grid) - 1 and j == len(grid) - 1:
                ans = max(ans, k)
            for _dir in dirs:
                i1, j1 = _dir
                newI = i + i1
                newJ = j + j1
                if isSafe(grid, newI, newJ) and grid[newI][newJ] == 0 and (newI, newJ) not in visited:
                    visited.add((newI, newJ))
                    graph.append((newI, newJ, (k if k != -1 else 1) + 1))
        return ans