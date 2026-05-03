class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 1
        if len(nums) == 1:
            return 1
        
        while j < len(nums) and i < len(nums):
            if nums[i] == nums[j]:
                if i > 0 and nums[i - 1] == nums[j]:
                    current = nums[j]
                    while j < len(nums) and nums[j] == current:
                        j += 1
                else:
                    i += 1
                    nums[i] = nums[j]
                    j += 1
            elif nums[i] < nums[j]:
                i += 1
                nums[i] = nums[j]
                j += 1
        return i + 1