class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        dp = [defaultdict(int) for _ in range(len(nums)+1)]
        dp[0][0] = 1

        for i in range(1, len(nums)+1):
            num = nums[i-1]
            for s, count in dp[i-1].items():
                dp[i][s-num] += count
                dp[i][s+num] += count
            
        return dp[-1][target]

        