class Solution:
    def trap(self, height: List[int]) -> int:
        i, j = 0, 1
        totalWater = 0
        highFromLeft = [0] * len(height)
        highFromRight = [0] * len(height)
        highFromLeft[0] = height[0]
        highFromRight[len(height)-1] = height[len(height)-1]

        for m in range(1, len(height)):
            if height[m] > highFromLeft[m - 1]:
                highFromLeft[m] = height[m]
            else:
                highFromLeft[m] = highFromLeft[m - 1]

        for m in range(len(height) - 2, -1, -1):
            if height[m] > highFromRight[m + 1]:
                highFromRight[m] = height[m]
            else:
                highFromRight[m] = highFromRight[m + 1]

        for m in range(1, len(height) - 1):
            _min = min(highFromLeft[m], highFromRight[m])
            if _min > height[m]:
                totalWater += _min - height[m]
        return totalWater