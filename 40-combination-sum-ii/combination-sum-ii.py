class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        self.retAns = []
        def helper(candidates, target, currentSum = 0, arr = [], i = 0):
            if currentSum == target:
                self.retAns.append(arr[:])
                return

            if i == len(candidates):
                return

            if currentSum > target:
                return

            arr.append(candidates[i])
            currentSum += candidates[i]
            helper(candidates, target, currentSum, arr, i + 1)

            arr.pop()
            currentSum -= candidates[i]
            while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
                i += 1
            helper(candidates, target, currentSum, arr, i + 1)


        helper(candidates, target)
        return self.retAns