class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        ans = []
        pacific = set()
        atlantic = set()
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def isSafe(heights, i, j):
            return not (i < 0 or j < 0 or i >= len(heights) or j >= len(heights[i]))

        def dfs(heights, i, j, visited):
            visited.add((i, j))

            for r, c in dirs:
                newR = i + r
                newC = j + c
                if isSafe(heights, newR, newC) and (newR, newC) not in visited and heights[newR][newC] >= heights[i][j]:
                    dfs(heights, newR, newC, visited)

        for i in range(m):
            dfs(heights, i, 0, pacific)
            dfs(heights, i, n - 1, atlantic)

        for i in range(n):
            dfs(heights, 0, i, pacific)
            dfs(heights, m - 1, i, atlantic)

        for i in range(m):
            for j in range(n):
                if (i, j) in pacific and (i, j) in atlantic:
                    ans.append([i, j])
        return ans