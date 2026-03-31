class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)
        self.res = []
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.time_map[key]
        if key in self.time_map:
            l = 0
            r = len(values) -1 
            
            while l <= r:
                mid = l + (r-l) // 2
                if values[mid][1] <= timestamp:
                    res = values[mid][0]
                    l = mid + 1
                else:
                    r = mid - 1


        return res

