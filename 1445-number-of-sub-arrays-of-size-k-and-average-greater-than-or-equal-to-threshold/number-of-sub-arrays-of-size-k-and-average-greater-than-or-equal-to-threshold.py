class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        target = threshold * k
        _sum = sum(arr[:k])
        ans = 0

        if _sum >= target:
            ans += 1

        for i in range(k, len(arr)):
            _sum = _sum - arr[i - k] + arr[i]
            if _sum >= target:
                ans += 1

        return ans