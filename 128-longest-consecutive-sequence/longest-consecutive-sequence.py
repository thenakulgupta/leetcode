class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmaps = {}
        results = 0
        for num in nums:
            hashmaps[num] = num
        for num in hashmaps.keys():
            if num-1 not in hashmaps:
                i = 0
                localResult = 0
                while True:
                    a = num + i
                    if a in hashmaps:
                        localResult += 1
                    else:
                        if results < localResult:
                            results = localResult
                        break
                    i+=1
        return results