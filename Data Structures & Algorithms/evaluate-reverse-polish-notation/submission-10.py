class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        for t in tokens:
            if t not in ("+", "-", "*", "/"):
                stack.append(int(t))
            else:
                num_2 = stack.pop()
                num_1 = stack.pop()
                if t == "+":
                    stack.append(num_1+num_2)
                elif t == "-":
                    stack.append(num_1-num_2)
                elif t == "*":
                    stack.append(num_1*num_2)
                elif t == "/":
                    stack.append(int(num_1/num_2))
        
        return stack[-1]