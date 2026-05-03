class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        i, j = 0, 0
        hm = {}
        runningCount = 0
        while i <= j and j < len(s):
            c = s[j]
            if c not in hm:
                hm[c] = 1
                j += 1
                runningCount += 1
                ans = max(ans, runningCount)
            else:
                while s[i] != s[j]:
                    del hm[s[i]]
                    i += 1
                    runningCount -= 1
                i += 1
                j += 1
        return ans