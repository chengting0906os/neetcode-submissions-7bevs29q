class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False
        """
            0   1   2   3
        0
        1
        2
        3               
        """
        dp = [[False] * (n+1) for _ in range(m+1)]
        dp[m][n] = True

        for i in range(m, -1, -1):
            for j in range(n, -1, -1):
                if i < m and s1[i] == s3[i+j] and dp[i+1][j] is True:
                    dp[i][j] = True
                if j < n and s2[j] == s3[i+j] and dp[i][j+1] is True:
                    dp[i][j] = True
        
        return dp[0][0]
        