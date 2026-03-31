class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        exponent = abs(n)
        base = x
        res = 1

        while exponent > 0:
            if exponent % 2 == 1:
                res *= base
            base *= base
            exponent //= 2

        return res if n > 0 else 1 / res

        
       