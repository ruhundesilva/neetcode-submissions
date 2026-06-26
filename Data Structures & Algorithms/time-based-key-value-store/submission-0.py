class TimeMap:

    def __init__(self):
        self.timeDict = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeDict[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeDict:
            return ""
        valList = self.timeDict[key]
        maxTime = 0
        maxValue = ""
        l, r = 0, len(valList) - 1
        while l <= r:
            mid = l + (r - l) // 2
            value, time = valList[mid]
            if time == timestamp:
                return value
            if time > timestamp:
                r = mid - 1
            else:
                if time > maxTime:
                    maxTime = time
                    maxValue = value
                l = mid + 1
        return maxValue
                
