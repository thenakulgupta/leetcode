class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        retArr = []
        nums = sorted(nums)

        def findSubsets(nums, arr=[], i=0):
            if i == len(nums):
                nonlocal retArr
                retArr.append(arr[:])
                return

            arr.append(nums[i])
            findSubsets(nums, arr, i + 1)

            arr.pop()
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            findSubsets(nums, arr, i + 1)

        findSubsets(nums)

        return retArr