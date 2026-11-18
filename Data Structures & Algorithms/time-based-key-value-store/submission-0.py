class TimeMap:

    def __init__(self):
        self.dictt = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dictt:
            self.dictt[key] = []
        self.dictt[key].append([value,timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        # normally we must return empty "" if nothing exists
        res = ""

        values = self.dictt.get(key,[])# [value,timestamp]

        l , r = 0 , len(values) - 1

        while(l <= r):
            m = (l+r)//2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m +1
            else:
                r = m -1

        
        return res
        
