class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while(len(stack) != 0 and temperatures[i] > temperatures[stack[-1]]):
                top = stack.pop()
                result[top] = i - top
            stack.append(i)
        return result