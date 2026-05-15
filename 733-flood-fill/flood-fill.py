class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.visited = set()
        startingPixel = image[sr][sc]
        dirs = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        def isSafe(image, i, j):
            return not (i < 0 or j < 0 or i >= len(image) or j >= len(image[i]))

        def dfs(image, i, j):
            if not isSafe(image, i, j):
                return

            if image[i][j] != startingPixel:
                return

            if (i, j) in self.visited:
                return

            image[i][j] = color
            self.visited.add((i, j))
            for _dir in dirs:
                i1, j1 = _dir
                newI = i + i1
                newJ = j + j1
                dfs(image, newI, newJ)

        dfs(image, sr, sc)
               
        return image