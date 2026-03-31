class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_res = 0
        lowest = float('inf')

        for p in prices:
            lowest = min(lowest, p)
            diff = p - lowest
            max_res = max(diff, max_res)
            
            
        
        return max_res