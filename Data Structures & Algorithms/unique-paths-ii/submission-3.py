class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        Plan: if obstacleGrid[i][j] == 0 dp[i][j] = 0

        Time Complexity: m * n
        Space Complexity: m * n
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [0] * n 

        for j in range(n):
            if obstacleGrid[0][j] == 1:
                break
            dp[j] = 1

        for i in range(1, m):
            if obstacleGrid[i][0] == 1:
                dp[0] = 0 
            
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                else:
                    dp[j] += dp[j-1]

        return dp[n-1]