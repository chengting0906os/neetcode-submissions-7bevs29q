class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Use a DP table to record whether each substring is a palindrome.
        Enumerate string by length(small to large) so shorter 
        results are ready when needed.
        Track the longest palindrome's start and length.
        """
        start = 0
        res_length = 1
        n = len(s)
        dp = [[False] * n for _ in range(n)] # dp[start][end] = False / True

        for i in range(n):
            dp[i][i] = True
        
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                start = i
                res_length = 2
        

        for length in range(3, n+1):
            for left in range(n - length + 1):
                right = left + length - 1
                if s[left] == s[right] and dp[left+1][right-1] is True:
                    dp[left][right] = True
                    if length > res_length:
                        res_length = length
                        start = left
        
        return s[start:start + res_length]
                    