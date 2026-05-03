class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hm = {0: 1}
        currentSum = 0
        count = 0
        for num in nums:
            currentSum += num
            if currentSum - k in hm:
                count += hm[currentSum - k]
            hm[currentSum] = hm.get(currentSum, 0) + 1
        return count