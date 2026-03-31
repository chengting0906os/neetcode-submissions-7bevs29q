class Solution:
    def longestPalindrome(self, s: str) -> str:
        count = 0
        res_s = ""
        n = len(s)

        # odd
        for i in range(n):
            temp_odd_res = 0
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                if l == r:
                    temp_odd_res += 1
                else:
                    temp_odd_res += 2
                
                if temp_odd_res > count:
                    count = temp_odd_res
                    res_s = s[l:r+1]
                l -= 1
                r += 1

        # even
        for i in range(1, n):
            temp_even_res = 0
            l = i - 1
            r = i 
            while l >= 0 and r < n and s[l] == s[r]:
                temp_even_res += 2
                if temp_even_res > count:
                    count = temp_even_res
                    res_s = s[l: r+1]
                l -= 1
                r += 1
        
        return res_s
                
        