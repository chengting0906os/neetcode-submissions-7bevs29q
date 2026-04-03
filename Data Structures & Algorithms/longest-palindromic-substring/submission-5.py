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
        
        for i in range(n):
            # odd
            l = i
            r = i
            while l >= 0 and r < n and s[l] == s[r]:
                if (r-l+1) > res_length:
                    start = l
                    res_length = r - l + 1
                l -= 1
                r += 1

            # even
            l = i
            r = i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                if (r-l+1) > res_length:
                    start = l
                    res_length = r - l + 1
                l -= 1
                r += 1
        return s[start:start+res_length]
