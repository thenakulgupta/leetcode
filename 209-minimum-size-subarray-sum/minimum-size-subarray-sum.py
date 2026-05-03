class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        currentSum = 0
        i = 0
        ans = float('INF')
        for j in range(len(nums)):
            currentSum += nums[j]
            while currentSum >= target:
                ans = min(ans, j - i + 1)
                currentSum -= nums[i]
                i += 1
            
        return ans if ans != float('INF') else 0