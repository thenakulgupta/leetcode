class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        uniqueVals = set()
        for num in nums:
            if num in uniqueVals:
                return True
            uniqueVals.add(num)
        return False