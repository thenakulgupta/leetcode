class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashmap = {}
        for _str in strs:
            _sorted = "".join(sorted(_str))
            if _sorted not in hashmap:
                hashmap[_sorted] = []
            hashmap[_sorted].append(_str)
        return hashmap.values()