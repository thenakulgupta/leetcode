class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) < 4 or len(s) > 12:
            return []
        self.retAns = []
        def checkIP(arr):
            maxToBeAdded = 4 * 3 - len(arr) * 3
            leftNow = (4 - len(arr)) * 3

            if leftNow > maxToBeAdded:
                return False

            if len(arr) > 4:
                return False

            if len(arr) > 0:
                lastEle = arr[-1]
                if len(lastEle) != len(str(int(lastEle))):
                    return False
                if int(lastEle) < 0 or int(lastEle) > 255:
                    return False
            return True
        def restoreIpAddressesHelper(s, i=0, arr=[]):
            if i == len(s):
                if len(arr) == 4 and sum([len(_) for _ in arr]) == len(s) and checkIP(arr):
                    self.retAns.append(".".join(arr))
                return True

            if not checkIP(arr):
                return False

            arr.append("")
            for j in range(i, min(i + 3, len(s))):
                lastEle = arr[-1]
                lastEle += s[j]
                arr[-1] = lastEle
                restoreIpAddressesHelper(s, j + 1, arr)
            arr.pop()
            return True
            

        restoreIpAddressesHelper(s)
        return self.retAns