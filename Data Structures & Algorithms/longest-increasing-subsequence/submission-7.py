class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        def bisect_left(a, x):
            lo, hi = 0, len(a)
            while lo < hi:
                mid = (lo + hi) // 2
                if a[mid] < x:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        dp = [nums[0]]
        LIS = 1

        for i in range(1, len(nums)):
            if dp[-1] < nums[i]:
                dp.append(nums[i])
                LIS += 1
                continue
            idx = bisect_left(dp, nums[i])
            dp[idx] = nums[i]

        return LIS