class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        cur_end = 0
        max_reach = 0


        # traverse to Second-to-last
        for i in range(n-1):
            max_reach = max(max_reach, i+nums[i])
            if i == cur_end:
                res += 1
                cur_end = max_reach
            
        return res
