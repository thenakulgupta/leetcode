class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hm = {}
        visited = set()
        for num in nums:
            hm[num] = 1

        ans = 0
        for num in nums:
            if num - 1 not in hm and num not in visited:
                curr = num
                curr_len = 0
                while curr in hm:
                    curr_len += 1
                    visited.add(curr)
                    curr += 1
                ans = max(ans, curr_len)
        return ans