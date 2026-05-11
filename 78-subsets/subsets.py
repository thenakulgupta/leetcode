class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        returnArr = list()
        def findSubsets(nums, ans=[], i=0):
            if i == len(nums):
                nonlocal returnArr
                returnArr.append(ans[:])
                return

            ans.append(nums[i])
            findSubsets(nums, ans, i + 1)

            ans.pop()
            findSubsets(nums, ans, i + 1)

        findSubsets(nums)
        return returnArr