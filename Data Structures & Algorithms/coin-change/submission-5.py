class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {0: 0}

        def dfs(rem):
            if rem in memo:
                return memo[rem]
            
            res = float('inf')
            for c in coins:
                sub = rem - c
                if sub >= 0:
                    res = min(res, 1 + dfs(sub))

            memo[rem] = res
            return res

        ans = dfs(amount)
        return ans if ans != float('inf') else -1

