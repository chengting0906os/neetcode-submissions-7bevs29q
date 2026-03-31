class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        bucket = set()
        res = 0
        l = 0
        r = 0 

        while r < len(s):
            if s[r] not in bucket:
                bucket.add(s[r])
                res = max(res, len(bucket))
                r += 1
            else:
                bucket.remove(s[l])
                l += 1
        return res
               