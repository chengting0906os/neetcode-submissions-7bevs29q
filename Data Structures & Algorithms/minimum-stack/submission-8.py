class MinStack:

    def __init__(self):
        self.min_n = float('inf')
        self.stack = []

        # 1, -2, -6, -1, -7
        # [0, -3, -4, 5, -1]
        # 1, -2, -6, -6, -7

    def push(self, val: int) -> None:
        if not self.stack:
            self.min_n = val
            self.stack.append(0)
        else:
            self.stack.append(val - self.min_n)
            if val < self.min_n:
                self.min_n = val

        
        

    def pop(self) -> None:
        if not self.stack:
            return
        pop = self.stack.pop()
        if pop < 0:
            self.min_n = self.min_n - pop
        
        
        

    def top(self) -> int:
        if not self.stack:
            return
        if self.stack[-1] > 0:
            return self.stack[-1] + self.min_n
        else:
            return self.min_n
        

    def getMin(self) -> int:
        return self.min_n
        
