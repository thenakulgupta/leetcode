class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        m, n = nums[0], len(nums)
        hm = {m: 1}
        if n <= k:
            for i in range(1, n):
                if m == nums[i]:
                    return True
            return False
        for i in range(1, n):
            new = nums[i]
            if i <= k:
                if new in hm:
                    return True
                hm[new] = hm.get(new, 0) + 1
                if m == new:
                    return True
                continue
            last = nums[i - k - 1]
            if hm[last] > 1:
                hm[last] -= 1
            else:
                del hm[last]
            if new in hm:
                return True
            hm[new] = 1
        return False