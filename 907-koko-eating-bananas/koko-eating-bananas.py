class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        i, j = 1, max(piles)
        ans = j
        while i <= j:
            mid = j - (j - i) // 2
            t = 0
            for m in piles:
                t += math.ceil(m / mid)
            if t <= h:
                ans = min(ans, mid)
                j = mid - 1
            else:
                i = mid + 1
        return ans