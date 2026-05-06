class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i, j = nums[0], nums[0]

        while True:
            i = nums[i]
            j = nums[nums[j]]
            if i == j:
                break

        i = nums[0]

        while i != j:
            i = nums[i]
            j = nums[j]
            
        return i