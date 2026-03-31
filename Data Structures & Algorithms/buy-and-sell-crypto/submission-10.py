class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0
        min_buy = prices[0]

        for i in range(1, len(prices)):
            max_p = max(max_p, prices[i] - min_buy)
            min_buy = min(min_buy, prices[i])
        
        return max_p