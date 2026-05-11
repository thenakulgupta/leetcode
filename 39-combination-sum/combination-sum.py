class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        outputArr = []
        def checkSum(candidates, target, arr = [], currentSum = 0 , i = 0):
            if i == len(candidates):
                return

            if currentSum == target:
                nonlocal outputArr
                outputArr.append(arr[:])
                return

            if currentSum > target:
                return

            arr.append(candidates[i])
            currentSum += candidates[i]
            checkSum(candidates, target, arr, currentSum, i)

            arr.pop()
            currentSum -= candidates[i]
            checkSum(candidates, target, arr, currentSum, i+1)

        checkSum(candidates, target)
        return outputArr