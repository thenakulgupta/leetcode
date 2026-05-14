class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [i + 1 for i in range(9)]
        self.retArr = []
        
        def combinationSum3Helper(nums, k, n, currentSum, i, arr):
            if currentSum == n and len(arr) == k:
                self.retArr.append(arr[:])
                return

            if i == len(nums) or len(arr) > k or currentSum > n:
                return

            currentSum += nums[i]
            arr.append(nums[i])
            combinationSum3Helper(nums, k, n, currentSum, i + 1, arr)

            currentSum -= nums[i]
            arr.pop()
            combinationSum3Helper(nums, k, n, currentSum, i + 1, arr)


        combinationSum3Helper(nums, k, n, 0, 0, [])
        return self.retArr