class Solution:
    def isValid(self, s: str) -> bool:
        mp = { 
            ']': '[',
            '}': '{',
            ')': '('
        }
        stack = deque()
        
        for char in s:
            if char not in mp:
                stack.append(char)
            else:
                if stack:
                    c = stack.pop()
                    if mp[char] == c:
                        continue
                return False

        return not stack
