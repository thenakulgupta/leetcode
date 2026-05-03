class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height)-1
        maxWater = 0
        while i < j:
            length = j - i
            h = min(height[j], height[i])
            maxWater = max(maxWater, h * length)
            if height[i] < height[j] or height[i] == height[j]:
                i += 1
            else:
                j -= 1
        return maxWater