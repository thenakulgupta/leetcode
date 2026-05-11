class Solution:
    def __init__(self):
        self.phone_board = {
            1: [],                2: ['a', 'b','c'],    3: ['d','e','f'],
            4: ['g','h','i'],     5: ['j','k','l'],     6: ['m','n','o'],
            7: ['p','q','r','s'], 8: ['t','u','v'],     9: ['w','x','y','z']
        }
    def letterCombinations(self, digits: str) -> List[str]:
        returnArr = []

        def helper(digits, s="", i=0):
            if i == len(digits):
                if len(s) > 0:
                    nonlocal returnArr
                    returnArr.append(s[:])
                    return
            
            digit = ord(digits[i]) - ord('0')
            for char in self.phone_board[digit]:
                s += char
                helper(digits, s, i + 1)
                s = s[:-1]
        
        helper(digits)

        return returnArr