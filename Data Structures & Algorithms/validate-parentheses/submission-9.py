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
                else:
                    return False
                if mp[char] != c:
                    return False

        return True if not stack else False
