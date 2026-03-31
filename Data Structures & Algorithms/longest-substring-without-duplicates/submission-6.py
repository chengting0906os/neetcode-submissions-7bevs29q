class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        res = 0
        l = 0

        for r , char in enumerate(s):
            if char in mp:
                l = max(mp[char]+1, l)
            mp[char] = r
            res = max(r-l+1, res)
        return res
        