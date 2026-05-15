class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        graph = deque([(sr, sc)])
        visited = set()
        visited.add((sr, sc))
        startingPixel = image[sr][sc]
        dirs = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        def isSafe(image, i, j):
            return not (i < 0 or j < 0 or i >= len(image) or j >= len(image[i]))
        
        while len(graph):
            i, j = graph.popleft()
            if image[i][j] != startingPixel:
                continue
            image[i][j] = color
            for _dir in dirs:
                i1, j1 = _dir
                newI = i + i1
                newJ = j + j1
                if isSafe(image, newI, newJ) and (newI, newJ) not in visited:
                    graph.append((newI, newJ))
                    visited.add((newI, newJ))
        return image