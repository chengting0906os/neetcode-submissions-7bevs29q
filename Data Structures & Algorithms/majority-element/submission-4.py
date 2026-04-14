class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        now = nums[0]
        count = 1

        for i in range(1, len(nums)):
            if nums[i] == now:
                count += 1    
            else:
                count -= 1    
                if count == 0:
                    now = nums[i]  
                    count += 1
        return now
            