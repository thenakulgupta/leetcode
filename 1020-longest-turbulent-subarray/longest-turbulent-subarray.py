class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1
        if len(arr) == 2:
            return 2 if arr[0] != arr[1] else 1
        
        i, j = 0, 1
        ans = 2 if arr[0] != arr[1] else 1
        while i < j and j < len(arr):
            if j == len(arr) - 1:
                break
            else:
                n0, n1, n2 = arr[j-1], arr[j], arr[j+1]
                if (n0 > n1 and n1 < n2) or (n0 < n1 and n1 > n2):
                    j += 1
                    ans = max(ans, j - i + 1)
                else:
                    i = j
                    j += 1
                    if arr[i] != arr[j]:
                        ans = max(ans, j - i + 1)

        return ans