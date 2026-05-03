class TimeMap:

    def __init__(self):
        self.hm = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hm:
            self.hm[key] = []
        self.hm[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        data = self.hm.get(key, None)
        if data:
            if(int(data[0][0]) > timestamp):
                return ""
            i, j = 0, len(data) - 1
            while i <= j:
                mid = j - (j - i) // 2
                midData = data[mid]
                ts = midData[0]
                if ts == timestamp:
                    return midData[1]
                elif ts > timestamp:
                    j = mid - 1
                else:
                    i = mid + 1
            return data[j][1]
        return ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)