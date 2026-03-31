class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        n = len(prices)
        res = 0

        while r < n:
            buy = prices[l]
            sell = prices[r]
            if sell > buy:
                res = max(res, sell - buy)
            else:
                l = r

            r += 1
        return res