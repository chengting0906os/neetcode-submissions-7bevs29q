class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.sum_of_squares(n)

        while slow != fast:
            fast = self.sum_of_squares(self.sum_of_squares(fast))
            slow = self.sum_of_squares(slow)
        
        return fast == 1

        
    
    def sum_of_squares(self, n: int):
        res = 0
        while n:
            last_num = n % 10
            res += (last_num * last_num)
            n = n // 10
        return res