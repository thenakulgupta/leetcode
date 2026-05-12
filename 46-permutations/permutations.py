class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.retArr = []
        def permuteHelper(nums, arr=[]):
            if 0 == len(nums):
                self.retArr.append(arr[:])
                return
            
            for i in range(len(nums)):
                arr.append(nums[i])
                permuteHelper(nums[:i]+nums[i+1:], arr)
                arr.pop()

        permuteHelper(nums)
        return self.retArr