class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [nums[0]]

        for i in range(1, len(nums)):
            if nums[i] > dp[-1]:
                dp.append(nums[i])
            else: 
                for j in range(len(dp)):
                    if dp[j] >= nums[i]:
                        dp[j] = nums[i]
                        break
        return len(dp)
