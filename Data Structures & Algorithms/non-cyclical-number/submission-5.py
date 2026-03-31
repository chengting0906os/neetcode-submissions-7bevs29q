class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n:
            if n == 1:
                return True
            if n in visited:
                return False

            visited.add(n)
            n = self.sum_of_squares(n)

            

        
    
    def sum_of_squares(self, n: int):
        res = 0
        while n:
            last_num = n % 10
            res += (last_num * last_num)
            n = n // 10
        return res