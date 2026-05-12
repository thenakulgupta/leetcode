class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.retArr = []
        def checkPalindrome(s):
            i, j = 0, len(s) - 1
            while i <= j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        def partitionHelper(s, i=0, arr=[]):
            if i == len(s):
                self.retArr.append(arr[:])
                return

            for end in range(i, len(s)):
                substr = s[i:end+1]
                if checkPalindrome(substr):
                    arr.append(substr)
                    partitionHelper(s, end + 1, arr)
                    arr.pop()

        partitionHelper(s)
        return self.retArr