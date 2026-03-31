from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = {}
        longest = 0

        for n in nums:
            if not mp.get(n, 0):

                left = mp.get(n - 1, 0)
                right = mp.get(n + 1, 0)

                length = left + 1 + right
                mp[n] = length

                # 更新區間的左右邊界
                mp[n - left] = length
                mp[n + right] = length

                longest = max(longest, length)

        return longest

