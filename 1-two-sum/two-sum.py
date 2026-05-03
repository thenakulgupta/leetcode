class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i in range(0, len(nums)):
            num = nums[i]
            sumLeft = target - num
            if sumLeft in hashmap:
                return [hashmap[sumLeft], i]
            hashmap[num] = i
        return []