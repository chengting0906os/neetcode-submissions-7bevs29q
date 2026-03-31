class Solution:
    def numDecodings(self, s: str) -> int:
        """
        Plan: 
            - s[0] == "0" return 0 
            - 空字串有一種解法
            - s[i-1] != 0 的時候 s[i] 完全繼承
            - s[i-2] 在 10 ~ 26 的時候 完全繼承 dp[i-2]

        Time Complexity: O(n)
        Space Complexity: O(n)
        1122
        (1,1,2,2)
        (1,12,2)
        (1,1,22)
        (11,2,2)
        (11,22)
        """
        if s[0] == "0":
            return 0
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, len(s)+1):
            if s[i-1] != "0":
                dp[i] += dp[i-1]

            two = s[i-2:i]
            if 10 <= int(two) <= 26:
                dp[i] += dp[i-2]

        return dp[-1]                
