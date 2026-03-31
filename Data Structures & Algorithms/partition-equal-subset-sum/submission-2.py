class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        n = len(nums)
        target = sum(nums) // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for n in nums:
            next_dp = dp[:]
            for i in range(n, target+1):
                next_dp[i] = next_dp[i] or dp[i-n]
            dp = next_dp
        
        return dp[target]