class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p = float('inf')
        res = 0

        for p in prices:
            min_p = min(p, min_p)
            res = max(res, p - min_p)
        
        return res