class Solution:
    def isNumber(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    def calculateVal(self, a, b, sym):
        if sym == "+":
            return a + b
        elif sym == "-":
            return a - b
        elif sym == "*":
            return a * b
        elif sym == "/":
            return int(a / b)

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if self.isNumber(t):
                stack.append(int(t))
            else:
                b = stack.pop()
                a = stack.pop()
                stack.append(self.calculateVal(a, b, t))
        return stack[0]