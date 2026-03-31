class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # cooldown and first day can sell and buy in next day
        # 買的隔天不能買 只能賣 or cooldown
        # 賣的隔天不能買 只能 cooldown

        
        def dfs(i, buying):
            if i >= len(prices):
                return 0

            cooldown = dfs(i+1, buying) 
            if buying:
                buy = dfs(i+1, False) - prices[i]
                return max(buy, cooldown) # 求出 第一天 buy 或 cooldown 的 max
            elif not buying:
                sell = dfs(i+2, True) + prices[i] # 賣隔天不能買，i+2 天可以買
                return max(sell, cooldown)

        return dfs(0, True)