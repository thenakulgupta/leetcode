class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        returnArr = []

        def helper(nums, ans=[]):
            if 0 == len(nums):
                nonlocal returnArr
                returnArr.append(ans[:])
                return
            
            for j in range(len(nums)):
                ans.append(nums[j])
                helper(nums[:j] + nums[j+1:], ans)
                ans.pop()

        helper(nums)

        return returnArr