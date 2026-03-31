class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        l = 0
        res = 0

        for r, char in enumerate(s):
            if char not in mp:
                mp[char] = r
            else:
                l = max(mp[char]+1, l)
                mp[char] = r

            res = max(r-l+1, res)

        return res
