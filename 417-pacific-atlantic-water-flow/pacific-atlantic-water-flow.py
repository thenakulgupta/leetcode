class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ans = []
        def isSafe(heights, i, j):
            return not (i < 0 or j < 0 or i >= len(heights) or j >= len(heights[i]))

        def isOceanSide(heights, i, j, _type):
            if _type == "pacific" and (j == 0 or i == 0):
                return True
            if _type == "atlantic" and (j == len(heights[i]) - 1 or i == len(heights) - 1):
                return True
            return False

        def dfs(heights, i, j, visited, _type):
            visited.add((i, j))
            dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            if isOceanSide(heights, i, j, _type):
                return True

            for r, c in dirs:
                newR = i + r
                newC = j + c
                if isSafe(heights, newR, newC) and (newR, newC) not in visited and heights[newR][newC] <= heights[i][j]:
                    if dfs(heights, newR, newC, visited, _type):
                        return True
            return False

        for i in range(len(heights)):
            for j in range(len(heights[i])):
                if dfs(heights, i, j, set(), "pacific") and dfs(heights, i, j, set(), "atlantic"):
                    ans.append([i, j])
        return ans