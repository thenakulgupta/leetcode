class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        retAns = []
        nums = [i for i in range(1, n + 1)]

        def findArrs(nums, k, arr=[], i=0):
            if k == len(arr):
                nonlocal retAns
                retAns.append(arr[:])
                return
            if i == len(nums):
                return
            
            arr.append(nums[i])
            findArrs(nums, k, arr, i + 1)

            arr.pop()
            findArrs(nums, k, arr, i + 1)
        
        findArrs(nums, k)

        return retAns