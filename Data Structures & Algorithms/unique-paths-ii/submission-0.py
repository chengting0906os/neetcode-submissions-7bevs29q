class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        Plan: if obstacleGrid[i][j] == 0 dp[i][j] = 0

        Time Complexity: m * n
        Space Complexity: m * n
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1

        for j in range(n):
            if obstacleGrid[0][j] == 1:
                break
            dp[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                count = 0
                if obstacleGrid[i-1][j] != 1:
                    count += dp[i-1][j]
                if obstacleGrid[i][j-1] != 1:
                    count += dp[i][j-1]
                if obstacleGrid[i][j] != 1:
                    dp[i][j] = count
        return dp[m-1][n-1]