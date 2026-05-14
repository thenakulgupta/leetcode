class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        self.reqArr = set()

        def numTilePossibilitiesHelper(tiles, i, s, visited):
            if i == len(tiles):
                return

            for j in range(len(tiles)):
                if j not in visited:
                    s += tiles[j]
                    self.reqArr.add(s)
                    visited.add(j)
                    numTilePossibilitiesHelper(tiles, i + 1, s, visited)
                    s = s[:-1]
                    visited.discard(j)

        numTilePossibilitiesHelper(tiles, 0, "", set())
        print(self.reqArr)
        return len(self.reqArr)