class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        returnData = []
        hashmap = {}
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 0
            hashmap[num] += 1
        for key, value in sorted(hashmap.items(), key = lambda item: item[1], reverse = True):
            if len(returnData) == k:
                break
            returnData.append(key)
        return returnData