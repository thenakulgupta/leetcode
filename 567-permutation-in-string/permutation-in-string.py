class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        need = [0] * 26
        window = [0] * 26

        # build need
        for c in s1:
            need[ord(c) - ord('a')] += 1

        matches = 0

        # initial window
        for i in range(len(s1)):
            idx = ord(s2[i]) - ord('a')
            window[idx] += 1

        # count initial matches
        for i in range(26):
            if need[i] == window[i]:
                matches += 1

        left = 0

        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True

            # add new char
            idx = ord(s2[right]) - ord('a')
            window[idx] += 1

            if window[idx] == need[idx]:
                matches += 1
            elif window[idx] == need[idx] + 1:
                matches -= 1

            # remove old char
            idx = ord(s2[left]) - ord('a')
            window[idx] -= 1

            if window[idx] == need[idx]:
                matches += 1
            elif window[idx] == need[idx] - 1:
                matches -= 1

            left += 1

        return matches == 26