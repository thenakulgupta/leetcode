class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.retArr = []
        nums = sorted(nums)

        def permuteUniqueHelper(nums, arr=[]):
            if 0 == len(nums):
                self.retArr.append(arr[:])
                return

            for i in range(len(nums)):
                if nums[i] != (nums[i-1] if i > 0 else nums[i] - 1):
                    arr.append(nums[i])
                    permuteUniqueHelper(nums[:i] + nums[i+1:], arr)
                    arr.pop()

        permuteUniqueHelper(nums)
        return self.retArr