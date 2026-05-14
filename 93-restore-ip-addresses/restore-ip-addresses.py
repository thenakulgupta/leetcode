class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) < 4 or len(s) > 12:
            return []
        self.retAns = []
        def checkIP(arr):
            if len(arr) > 4:
                return False

            if len(arr) > 0:
                lastEle = arr[-1]
                if len(lastEle) > 1 and lastEle[0] == '0':
                    return False
                if int(lastEle) < 0 or int(lastEle) > 255:
                    return False
            return True
        def restoreIpAddressesHelper(s, i=0, arr=[]):
            if i == len(s):
                if len(arr) == 4:
                    self.retAns.append(".".join(arr))
                return

            if not checkIP(arr):
                return

            arr.append("")
            for j in range(i, min(i + 3, len(s))):
                arr[-1] = s[i:j+1]
                if checkIP(arr):
                    restoreIpAddressesHelper(s, j + 1, arr)
            arr.pop()
            

        restoreIpAddressesHelper(s)
        return self.retAns