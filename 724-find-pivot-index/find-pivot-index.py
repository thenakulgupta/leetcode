class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum, rightSum = [nums[0]] * len(nums), [nums[len(nums)-1]] * len(nums)
        for i in range(1, len(nums)):
            leftSum[i] = leftSum[i-1] + nums[i]
        for i in range(len(nums)-2, -1, -1):
            rightSum[i] = rightSum[i+1] + nums[i]
        for i in range(len(nums)):
            if leftSum[i] == rightSum[i]:
                return i
        return -1