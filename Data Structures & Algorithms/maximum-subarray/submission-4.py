class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
    
        n = len(nums)
        dp = [[0]*2 for _ in range(n)]
        """
        [
        [0,0],
        [0,0],
        [0,0],
        [0,0]
        ]
        """
        dp[0][0] = nums[0]
        dp[0][1] = nums[0]

        for i in range(1, n):
            dp[i][0] = max(nums[i] + dp[i-1][0], nums[i]) 
            dp[i][1] = max(dp[i][0], dp[i-1][1])

        
        return dp[-1][1]