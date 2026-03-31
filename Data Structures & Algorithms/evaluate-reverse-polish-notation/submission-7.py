class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        for t in tokens:
            if t not in ("+", "-", "*", "/"):
                stack.append(t)
            else:
                num_2 = int(stack.pop())
                num_1 = int(stack.pop())
            if t == "+":
                stack.append(num_1+num_2)
            elif t == "-":
                stack.append(num_1-num_2)
            elif t == "*":
                stack.append(num_1*num_2)
            elif t == "/":
                stack.append(num_1/num_2)
        
        return int(stack[-1])