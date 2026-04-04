class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sum = nums[0]
        cur_sum = nums[0]
        total = nums[0]
        min_sum = nums[0]
        cur_min = nums[0]

        for n in nums[1:]:
            cur_sum = max(cur_sum + n, n)
            max_sum = max(cur_sum, max_sum)
            total += n
            cur_min = min(cur_min + n, n)
            min_sum = min(cur_min, min_sum)
        
        return max_sum if max_sum < 0 else max(max_sum, total - min_sum)