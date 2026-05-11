class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        retArr=[]
        def helper(nums, arr=[]):
            if 0 == len(nums):
                nonlocal retArr
                retArr.append(arr[:])

            for i in range(len(nums)):
                if nums[i] != (nums[i - 1] if i > 0 else nums[i] - 1):
                    arr.append(nums[i])
                    helper(nums[:i] + nums[i+1:], arr)
                    arr.pop()

        helper(nums)
        return retArr