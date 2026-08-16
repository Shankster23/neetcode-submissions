class TimeMap:

    def __init__(self):
        self.hash_map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hash_map:
            self.hash_map[key] = []
        self.hash_map[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hash_map:
            return ""
        res = ""
        values = self.hash_map[key]
        lo, hi = 0, len(self.hash_map[key]) - 1
        while lo <= hi:
            mid = lo+ (hi - lo)//2
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                lo = mid + 1
            else:
                hi = mid - 1
        return res



        
