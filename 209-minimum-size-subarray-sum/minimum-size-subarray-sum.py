class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        ans = float("inf")
        currentSum = nums[0]
        i, j = 0, 0
        if n == 1:
            return 1 if nums[0] >= target else 0
        while True:
            if currentSum == target or currentSum < target:
                if currentSum == target:
                    ans = min(ans, j - i + 1)
                if j != n - 1:
                    j += 1
                    currentSum += nums[j]
                elif i != n - 1:
                    currentSum -= nums[i]
                    i += 1
                else:
                    break
            else:
                ans = min(ans, j - i + 1)
                if i != n - 1:
                    currentSum -= nums[i]
                    i += 1
                else:
                    break
        return ans if ans != float("inf") else 0