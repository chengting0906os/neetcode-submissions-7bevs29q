class Solution:
    def myPow(self, x: float, n: int) -> float:
        # if n == 0:
        #     return 1.0
        # exponent = abs(n)

        # # brutal
        # res = 1
        # for _ in range(exponent):
        #     res *= x
        
        # return res if n > 0 else (1 / res)

        # recursive
        # 7 -> 3 -> 1 

        def dfs(x, exponent):
            if exponent == 0:
                return 1
            
            if x == 0:
                return 0

            
            half = dfs(x,  exponent//2)

            if exponent % 2 == 1:
                return half * half * x
            else:
                return half * half

        
        res = dfs(x, abs(n))
        
        return res if n >= 0 else 1 / res
   


        # iterative