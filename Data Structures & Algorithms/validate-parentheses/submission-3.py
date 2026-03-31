class Solution:
    def isValid(self, s: str) -> bool:
        mp = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        stack = []

        for char in s:
            if char in mp:
                if stack and stack[-1] == mp[char]:
                    stack.pop()
                else:
                    return False        
            else:
                stack.append(char)
            
        if not stack:
            return True
        
        else:
            return False
