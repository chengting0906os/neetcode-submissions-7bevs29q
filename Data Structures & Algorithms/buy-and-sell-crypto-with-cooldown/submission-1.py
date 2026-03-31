class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # cooldown and first day can sell and buy in next day
        # 買的隔天不能買 只能賣 or cooldown
        # 賣的隔天不能買 只能 cooldown
        memo = {}
        
        def dfs(i, buying):
            
            if i >= len(prices):
                return 0
            if (i, buying)in memo:
                return memo[(i, buying)]

            cooldown = dfs(i+1, buying) # buying might be True or False
            if buying:
                buy = dfs(i+1, False) - prices[i]
                memo[(i, buying)] =  max(buy, cooldown) # 求出 第一天 buy 或 cooldown 的 max
            elif not buying:
                sell = dfs(i+2, True) + prices[i] # 賣隔天不能買，i+2 天可以買
                memo[(i, buying)] = max(sell, cooldown)
            
            return memo[(i, buying)]

        return dfs(0, True)