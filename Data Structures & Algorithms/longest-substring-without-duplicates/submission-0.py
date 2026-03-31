class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            sub_string = 0
            bucket = set()
            while i >= 0:
                if s[i] not in bucket:
                    bucket.add(s[i])
                    sub_string += 1
                    res = max(sub_string, res)
                    i -= 1
                else:
                    break
                

        return res
