class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.retArr = []

        def combinationSum(candidates, target, i, currentSum, arr):
            if i == len(candidates):
                return

            if currentSum == target:
                self.retArr.append(arr[:])
                return

            if currentSum > target:
                return

            currentSum += candidates[i]
            arr.append(candidates[i])
            combinationSum(candidates, target, i, currentSum, arr)

            currentSum -= candidates[i]
            arr.pop()
            combinationSum(candidates, target, i + 1, currentSum, arr)


        combinationSum(candidates, target, 0, 0, [])
        return self.retArr