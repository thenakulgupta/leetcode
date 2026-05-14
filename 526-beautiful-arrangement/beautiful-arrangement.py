class Solution:
    def countArrangement(self, n: int) -> int:
        self.result = 0
        nums = [_ for _ in range(1, n + 1)]

        def checkBeautifulArrangement(arr):
            for i in range(1, len(arr) + 1):
                if not (arr[i - 1] % i == 0 or i % arr[i - 1] == 0):
                    return False
            return True

        def countArrangementHelper(nums, arr):
            if 0 == len(nums):
                self.result += 1
                return

            for i in range(len(nums)):
                arr.append(nums[i])
                if checkBeautifulArrangement(arr):
                    countArrangementHelper(nums[:i] + nums[i+1:], arr)
                arr.pop()

        countArrangementHelper(nums,[])

        return self.result