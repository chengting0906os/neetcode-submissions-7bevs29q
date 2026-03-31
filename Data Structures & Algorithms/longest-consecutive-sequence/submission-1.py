class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        res = 0
        start_num_mp = {}

        for n in nums:
            count = 0
            if n-1 not in nums:
                temp_n = n
                while temp_n in nums:
                    count +=1
                    temp_n +=1
                res = max(res, count)
        
        return res