from bisect import bisect_left
class TimeMap:

    def __init__(self):
        self.keys = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keys[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if not self.keys[key]:
            return ""
        i = bisect_left(self.keys[key], (timestamp, "#"))
        
        if i == len(self.keys[key]):
            return self.keys[key][-1][1]
        
        if self.keys[key][i][0] == timestamp:
            return self.keys[key][i][1]
        
        return self.keys[key][i-1][1] if i > 0 else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)