class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [nums[0]]

        for i in range(1, len(nums)):
            if nums[i] > dp[-1]:
                dp.append(nums[i])
            # replace first nums[i] >= dp[j] and 
            else:
                left = 0
                right = len(dp) - 1
                
                while left <= right:
                    mid = (right - left) // 2 + left 
                    if dp[mid] >= nums[i]:
                        right = mid - 1
                    else:
                        left = mid + 1

                dp[left] = nums[i]

        return len(dp)