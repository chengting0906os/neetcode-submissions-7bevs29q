class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        # 如果 -1 的不在才開始 while loop 計算
        for n in nums:
            cons = 0
            if n - 1 not in nums:
                base = n
                while base in nums:
                    cons += 1
                    base += 1
                    longest = max(longest, cons)
            
        return longest
