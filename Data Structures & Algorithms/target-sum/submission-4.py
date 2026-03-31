from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums, target):
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]

        # 初始化：用 nums[0]
        if nums[0] == 0:
            dp[0][0] = 2
        else:
            dp[0][nums[0]] = 1
            dp[0][-nums[0]] = 1

        for i in range(1, n):
            for s, count in dp[i-1].items():
                dp[i][s + nums[i]] += count
                dp[i][s - nums[i]] += count

        return dp[n-1][target]

        