class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [0] * (amount+1)
        dp[0] = 1

        for i in range(1, n+1):
            last_dp = dp[:]
            cur_coin = coins[i - 1]
            for a in range(amount+1):
                if a >= cur_coin:
                    dp[a] = last_dp[a] + dp[a-cur_coin]

        return dp[amount]