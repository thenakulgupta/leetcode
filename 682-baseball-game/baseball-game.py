class Solution:
    def isOperation(self, op):
        return op == "C" or op == "D" or op == "+"

    def calPoints(self, operations: List[str]) -> int:
        arr = []
        for op in operations:
            if self.isOperation(op):
                if op == "C":
                    arr.pop()
                if op == "D":
                    arr.append(arr[len(arr)-1] * 2)
                if op == "+":
                    arr.append(arr[len(arr)-1] + arr[len(arr)-2])
            else:
                arr.append(int(op))
        return sum(arr)