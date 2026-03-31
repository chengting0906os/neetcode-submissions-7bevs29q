class StockSpanner:

    def __init__(self):
        self.stack = []
        

    def next(self, price: int) -> int:
        res = 0 
        self.stack.append(price)
        i = len(self.stack) - 1
        while i >= 0:
            if self.stack[i] <= price:
                res += 1
                i -= 1
            else:
                break
        return res

        
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)