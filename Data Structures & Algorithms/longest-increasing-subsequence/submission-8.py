
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Plan:   1. 遍歷往右，再往回找 dp 紀錄，如果有就加上去
                2. binary search
        Time Complexity: n^2, nlogn
        Space Complexity: n
        """

        dp = []
        for n in nums:
            idx = self.my_bisect_left(dp, n)
            if idx == len(dp):
                dp.append(n)
            else:
                dp[idx] = n
            

        return len(dp)
    
    def my_bisect_left(self, my_list: List[int], num: int) -> int:
        l = 0
        r = len(my_list)

        while l < r:
            mid = l + (r - l) // 2
            if my_list[mid] < num:
                l = mid + 1
            else:
                r = mid

        return l