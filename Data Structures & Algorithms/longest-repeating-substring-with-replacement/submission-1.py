class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        maxf = 0
        mp = {}
        l = 0

        for r, char in enumerate(s):
            mp[char] = mp.get(char, 0) + 1
            maxf = max(maxf, mp[char])
            
            while (r - l + 1 - maxf) > k:
                mp[s[l]] -= 1
                l += 1
            res = max(r-l+1, res)

        
        return res