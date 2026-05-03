class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [-1] * len(nums) * 2
        for i in range(len(nums)):
            ans[i] = ans[len(nums) + i] = nums[i]
        return ans