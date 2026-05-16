class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        currSum = 0
        freq = {0: 1}
        count = 0
        for num in nums:
            currSum += num
            if currSum - k in freq:
                count += freq[currSum - k]
            freq[currSum] = freq.get(currSum, 0) + 1
        return count