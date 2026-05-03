class Solution:
    def isAlphaNumeric(self, s):
        num = ord(s)
        return (num >= 65 and num <= 90) or (num >= 97 and num <= 122) or (num >= 48 and num <= 57)

    def isPalindrome(self, s: str) -> bool:
        s = "".join(_.lower() if self.isAlphaNumeric(_) else "" for _ in s)
        i, j = 0, len(s) - 1
        while i <= j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True