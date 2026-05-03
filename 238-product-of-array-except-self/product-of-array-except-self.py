class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        leftMultiple = nums[0]
        output = [a for a in nums]
        for i in range(len(output)-2, 0, -1):
            output[i] = output[i] * output[i+1]
        output[0] = output[1]
        for i in range(1, len(nums)):
            output[i] = (1 if i == len(output)-1 else output[i+1]) * leftMultiple
            leftMultiple *= nums[i]
        return output