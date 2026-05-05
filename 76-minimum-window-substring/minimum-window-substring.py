class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        window = {}
        ans = float("inf")
        res = ""
        req = len(need)
        formed = 0
        left = 0
        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1

            if c in need and window[c] == need[c]:
                formed += 1

            while formed == req:
                if right - left + 1 < ans:
                    ans = right - left + 1
                    res = s[left : right + 1]

                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1
                left += 1
        return res