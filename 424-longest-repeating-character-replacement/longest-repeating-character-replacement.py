class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hm = {s[0]:1}
        ans = 1
        window_size = 1
        max_freq = 1
        i, j = 0, 1
        while i <= j and j < len(s):
            c = s[j]
            hm[c] = hm.get(c, 0) + 1
            window_size += 1
            max_freq = max(max_freq, hm[c])
            if window_size - max_freq > k:
                _c = s[i]
                if hm[_c] == 1:
                    del hm[_c]
                else:
                    hm[_c] -= 1
                window_size -= 1
                i += 1

            ans = max(ans, window_size)
            j += 1
        return ans