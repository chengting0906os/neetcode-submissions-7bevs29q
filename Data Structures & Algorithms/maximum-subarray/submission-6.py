class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = float('-inf')
        max_sum = float('-inf')

        """
            1   2   3   4   5
        cur
        max
        """

        for i in range(len(nums)):
            cur_sum = max(nums[i] + cur_sum, nums[i])
            max_sum = max(max_sum, cur_sum)
        
        return max_sum