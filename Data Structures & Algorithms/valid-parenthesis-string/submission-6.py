class Solution:
    def checkValidString(self, s: str) -> bool:
        min_open_needed = 0 # "(" 當前最少需要幾個
        open_max = 0 # "(" 目前未匹配的數量, "*" 可以當空字串


        for char in s:
            if char == '(':
                min_open_needed += 1
                open_max += 1
            if char == ')':
                min_open_needed -= 1
                open_max -= 1
            if char == '*':
                min_open_needed += 1
                open_max -= 1
            
            if min_open_needed < 0:
                return False
            
            if open_max < 0:
                open_max = 0 
        

        return open_max == 0