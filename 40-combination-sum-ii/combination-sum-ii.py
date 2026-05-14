class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        self.retArr = []

        def combinationSum2Helper(candidates, target, currentSum, i, arr):
            if target == currentSum:
                self.retArr.append(arr[:])
                return

            if i == len(candidates):
                return

            if currentSum > target:
                return

            currentSum += candidates[i]
            arr.append(candidates[i])
            combinationSum2Helper(candidates, target, currentSum, i + 1, arr)

            currentSum -= candidates[i]
            arr.pop()
            while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
                i += 1
            combinationSum2Helper(candidates, target, currentSum, i + 1, arr)

        combinationSum2Helper(candidates, target, 0, 0, [])
        return self.retArr