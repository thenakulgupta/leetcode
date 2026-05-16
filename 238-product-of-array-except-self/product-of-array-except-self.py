class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixMultiple = nums[0]
        outputArr = [0] * len(nums)
        for i in range(len(nums) - 1, 0, -1):
            outputArr[i] = nums[i] * (outputArr[i + 1] if i + 1 != len(outputArr) else 1)

        outputArr[0] = outputArr[1]
        
        for i in range(1, len(nums)):
            outputArr[i] = prefixMultiple * (outputArr[i + 1] if i + 1 != len(outputArr) else 1)
            prefixMultiple *= nums[i]

        return outputArr