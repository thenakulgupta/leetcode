class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.retArr = []

        def helper(n, i = 0, count = 0, s = ""):
            if i == n * 2:
                if count == 0:
                    self.retArr.append(s[:])
                return
            
            s += "("
            helper(n, i + 1, count + 1, s)

            s = s[:-1]

            if count > 0:
                s += ")"
                helper(n, i + 1, count - 1, s)
        
        helper(n)
        return self.retArr