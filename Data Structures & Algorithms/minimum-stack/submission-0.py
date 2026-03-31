class MinStack:

    def __init__(self):
        self.stack = []
        self.min_num = float('inf')
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_num = min(val, self.min_num)
        
    def pop(self) -> None:
        if self.stack:
            pop_num = self.stack.pop()
            if self.min_num == pop_num and self.stack:
                self.min_num = min(self.stack)
            
            if not self.stack:
                self.min_num = float('inf')
        
        
    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        return self.min_num
        
