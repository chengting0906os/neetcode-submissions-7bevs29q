class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        end = 0
        max_reach = 0

        for i in range(n - 1):
            max_reach = max(max_reach, i + nums[i])

            if i == end:
                res += 1
                end = max_reach

        return res
