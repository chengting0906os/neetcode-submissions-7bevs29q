class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1 and nums[0] >= 1:
            return 0

        max_reach = 0
        res = 0
        i = 0
        j = 0

        while j < len(nums)-1:
            max_reach = 0
            for i in range(i, j+1):
                max_reach = max(max_reach, nums[i] + i)
                
            res += 1
            i = j+1
            j = max_reach 
          

        return res
            
