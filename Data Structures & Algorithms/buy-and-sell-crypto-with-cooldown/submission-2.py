from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0

        hold = -prices[0]
        sell = 0
        cool = 0 

        for i in range(1, len(prices)):
            pre_hold = hold
            pre_sell = sell
            pre_cool = cool

            hold = max(pre_cool - prices[i], pre_hold)
            sell = pre_hold + prices[i]
            cool = max(pre_cool, pre_sell)

        return max(sell, cool)