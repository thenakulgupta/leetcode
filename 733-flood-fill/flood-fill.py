class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        stColor = image[sr][sc]
        def floodFillHelper(image, sr, sc, color, stColor):
            if sr < 0 or sc < 0 or sr >= len(image) or sc >= len(image[0]):
                return
            if image[sr][sc] != stColor or image[sr][sc] == color:
                return

            directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
            image[sr][sc] = color
            for direction in directions:
                row, col = direction
                floodFillHelper(image, sr + row, sc + col, color, stColor)


        floodFillHelper(image, sr, sc, color, stColor)
        return image