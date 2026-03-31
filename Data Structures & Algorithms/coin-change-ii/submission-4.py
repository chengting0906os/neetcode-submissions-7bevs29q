class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        memo = [[-1] * (amount + 1) for _ in range(len(coins) + 1)]

        def dfs(i, rem):
            if rem == 0:
                return 1
            if i >= len(coins):
                return 0
            if memo[i][rem] != -1:
                return memo[i][rem]

            res = 0
            if rem >= coins[i]:
                res = dfs(i + 1, rem)
                res += dfs(i, rem - coins[i])

            memo[i][rem] = res
            return res

        return dfs(0, amount)
