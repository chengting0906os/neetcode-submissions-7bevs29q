class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        res = float('-inf')
        
        for i in range(n):
            for j in range(i+1, n+1):
                res = max(res, sum(nums[i:j]))
        
        return res
