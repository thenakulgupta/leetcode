class Solution:
    def trap(self, height: List[int]) -> int:
        leftArr, rightArr = [0] * len(height), [0] * len(height)
        leftArr[0] = height[0]
        rightArr[-1] = height[-1]
        ans = 0

        for i in range(1, len(height)):
            leftArr[i] = max(leftArr[i - 1], height[i])
        for i in range(len(height) - 2, -1, -1):
            rightArr[i] = max(height[i], rightArr[i + 1])
        for i in range(1, len(height) - 1):
            ans += min(leftArr[i], rightArr[i]) - height[i]

        return ans