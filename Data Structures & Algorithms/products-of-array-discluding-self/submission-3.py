class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        # 第一步：建前綴積
        for left in range(1, n):
            result[left] = result[left-1] * nums[left-1]

        # 第二步：從右邊乘入後綴積
        right = nums[-1]
        for j in range(n-2, -1, -1):
            result[j] *= right
            right *= nums[j]

        return result