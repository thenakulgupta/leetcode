class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        arr = []
        nums = sorted(nums)

        for m in range(len(nums)):
            if m > 0 and nums[m-1] == nums[m]:
                continue

            i, j = m+1, len(nums)-1
            target = 0 - nums[m]
            while i < j:
                _sum = nums[i] + nums[j]
                if _sum < target:
                    i += 1
                elif _sum > target:
                    j -= 1
                else:
                    arr.append([nums[m], nums[i], nums[j]])
                    while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                        i += 1
                    while j > 1 and nums[j] == nums[j - 1]:
                        j -= 1
                    i += 1
                    j -= 1

        return arr