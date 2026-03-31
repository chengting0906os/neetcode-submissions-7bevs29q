class Solution:
    def rob(self, nums: List[int]) -> int:
        
        
        def helper(n_list):
            rob1, rob2 = 0, 0

            for n in n_list:
                temp = max(rob1+n, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2

        return max(nums[0], helper(nums[:-1]), helper(nums[1:]))