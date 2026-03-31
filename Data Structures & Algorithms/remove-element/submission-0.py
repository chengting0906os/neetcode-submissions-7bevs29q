class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        l = 0
        # [1,1,2,3,4]
        #       0
        # 0, 1, 2

        for r, n in enumerate(nums):
            if n == val:
                continue
            nums[l] = nums[r]
            l += 1
        
        nums = nums[:l]
        return l
        