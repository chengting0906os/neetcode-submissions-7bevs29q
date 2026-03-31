class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.sum_of_square(n)
        while slow != fast:
            fast = self.sum_of_square(fast)
            fast = self.sum_of_square(fast)
            slow = self.sum_of_square(slow)
        
        return fast == 1 

    


    def sum_of_square(self, n):
        res = 0
        while n:
            rem = n % 10
            res += rem * rem
            n = n // 10

        return res