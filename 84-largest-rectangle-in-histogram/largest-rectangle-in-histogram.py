class Solution:
    def previousSmallestNumbers(self, h):
        if not h:
            return []
        res = [-1]
        stack = [0]
        for i in range(1, len(h)):
            while len(stack) > 0 and h[stack[-1]] >= h[i]:
                stack.pop()
            if len(stack) > 0:
                res.append(stack[-1])
            else:
                res.append(-1)
            stack.append(i)
        return res

    def nextSmallestNumbers(self, h):
        if not h:
            return []
        res = [-1] * len(h)
        stack = []
        for i in range(len(h)-1, -1, -1):
            while len(stack) > 0 and h[stack[-1]] >= h[i]:
                stack.pop()
            if len(stack) > 0:
                res[i] = stack[-1]
            stack.append(i)
        return res
        

    def largestRectangleArea(self, heights: List[int]) -> int:
        psn = self.previousSmallestNumbers(heights)
        nsn = self.nextSmallestNumbers(heights)
        ans = 0
        for i in range(len(heights)):
            lIndex = psn[i] if psn[i] != -1 else -1
            rIndex = nsn[i] if nsn[i] != -1 else len(heights)
            print(rIndex, lIndex,  heights[i])
            ans = max(ans, (rIndex - lIndex - 1) * heights[i])
        return ans