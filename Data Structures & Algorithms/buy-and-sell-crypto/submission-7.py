class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        res = 0
        
        for i in range(n-1):
            buy = prices[i]
            for j in range(i+1, n):
                sell = prices[j]
                earn = sell - buy
                if earn > 0:
                    res = max(res, earn)
        
        return res