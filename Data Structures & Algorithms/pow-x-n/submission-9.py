class Solution:
    def myPow(self, x: float, n: int) -> float:
        # def dfs(x, exponent):
        #     if exponent == 0:
        #         return 1            
        #     if x == 0:
        #         return 0
        #     half = dfs(x,  exponent//2)
        #     if exponent % 2 == 1:
        #         return half * half * x
        #     else:
        #         return half * half
        # res = dfs(x, abs(n))
        # return res if n >= 0 else 1 / res
   
        # iterative

        if x == 0:
            return 0
        if n == 0:
            return 1

        exponent = abs(n) 
        res = 1
        
        while exponent > 0:
            if exponent % 2 == 1:
                res *= x
            x *= x
            exponent //= 2
        
        return res if n > 0 else 1 / res
        
       