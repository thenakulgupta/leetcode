class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        current_min = prices[0]
        for i in range(1, len(prices)):
            if current_min < prices[i]:
                ans = max(ans, prices[i] - current_min)
            else:
                current_min = prices[i]
        return ans