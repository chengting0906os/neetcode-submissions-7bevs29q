class MinStack:

    def __init__(self):
        self.stack = deque()
        self.min_stack = deque()
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_stack:
            min_v = min(self.min_stack[-1], val)
        else:
            min_v = val
        self.min_stack.append(min_v)
        
    def pop(self) -> None:
        if self.min_stack and self.stack:
            self.min_stack.pop()
            return self.stack.pop()
        

    def top(self) -> int:
        if self.min_stack and self.stack:
            return self.stack[-1]
        

    def getMin(self) -> int:
        if self.min_stack and self.stack:
            return self.min_stack[-1]
        
