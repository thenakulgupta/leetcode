class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        current_min = prices[0]
        for p in prices:
            if current_min < p:
                ans = max(ans, p - current_min)
            else:
                current_min = p
        return ans