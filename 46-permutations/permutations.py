class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        returnArr = []

        def helper(nums, ans=[], i=0):
            if i == len(nums):
                nonlocal returnArr
                returnArr.append(ans[:])
                return
            
            for j in range(len(nums)):
                if nums[j] not in ans:
                    ans.append(nums[j])
                    helper(nums, ans, i + 1)
                    ans.pop()

        helper(nums)

        return returnArr