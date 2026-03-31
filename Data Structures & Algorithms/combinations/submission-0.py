class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []

        def backtracking(i, curr):
            if len(curr) == k:
                res.append(curr.copy())
                return 
            
            for j in range(i, n+1):
                curr.append(j)
                backtracking(j+1, curr)
                curr.pop()

        
        backtracking(1, curr=[])
        return res