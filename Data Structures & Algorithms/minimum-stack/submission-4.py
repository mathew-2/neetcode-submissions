class MinStack:

    def __init__(self):
        self.arr = []
        self.minn = []


    def push(self, val: int) -> None:
        self.arr.append(val)
        val = min(val,self.minn[-1] if self.minn else val)
        self.minn.append(val)
        

    def pop(self) -> None:
        self.arr.pop()
        self.minn.pop()
        

    def top(self) -> int:
        return self.arr[-1]
        

    def getMin(self) -> int:
        return self.minn[-1]

        
