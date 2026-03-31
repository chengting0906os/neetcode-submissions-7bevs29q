class Solution:
    def isValid(self, s: str) -> bool:
        mp = { 
            ']': '[',
            '}': '{',
            ')': '('
        }
        stack = deque()
        
        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            else:
                if stack:
                    c = stack.pop()
                    if mp[char] == c:
                        continue
                return False

        return True if not stack else False
