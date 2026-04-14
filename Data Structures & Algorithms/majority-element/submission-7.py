class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        now = 0
        count = 0
        
        # 1, 5, 1
        for n in nums:
            if count == 0:
                now = n
            
            if now == n:
                count += 1
            else:
                count -= 1
        
        return now