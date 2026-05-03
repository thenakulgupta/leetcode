class Solution:
    def isClosable(self, v, s):
        if v == "(" and s == ")":
            return True
        elif v == "[" and s == "]":
            return True
        elif v == "{" and s == "}":
            return True
        return False

    def isValid(self, s: str) -> bool:
        if len(s) == 1 or len(s) % 2 != 0:
            return False
        arr = [_ for _ in s]
        openParentheses = ["(", "[", "{"]
        i = 0
        while True:
            if i >= len(arr):
                break
            if arr[i] not in openParentheses and i != 0:
                if not self.isClosable(arr[i-1], arr[i]):
                    return False
                else:
                    arr = arr[:i-1] + arr[i+1:]
                    i -= 2
            i += 1
        return len(arr) == 0