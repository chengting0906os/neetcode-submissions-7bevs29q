class Solution:
    def checkValidString(self, s: str) -> bool:
        open_min = 0 # "(" 當前最少需要幾個
        open_max = 0 # "(" 未被抵銷的數量


        for char in s:
            if char == '(':
                open_min += 1
                open_max += 1
            if char == ')':
                open_min -= 1
                open_max -= 1
            if char == '*':
                open_min += 1
                open_max -= 1
            
            if open_min < 0:
                return False
            
            if open_max < 0:
                open_max = 0 
        

        return open_max == 0