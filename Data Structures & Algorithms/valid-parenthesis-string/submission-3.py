class Solution:
    def checkValidString(self, s: str) -> bool:
        close_min = 0 
        open_max = 0


        for char in s:
            if char == '(':
                close_min += 1
                open_max += 1
            if char == ')':
                close_min -= 1
                open_max -= 1
            if char == '*':
                close_min += 1
                open_max -= 1
            
            if close_min < 0:
                return False
            
            if open_max < 0:
                open_max = 0 
        

        return open_max == 0