class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_l = height[l]
        max_r = height[r]
        res = 0

        while l < r:
            if height[l] <= height[r]:
                res += (max_l - height[l])
                l += 1
                max_l = max(height[l], max_l)
            else:
                res += (max_r - height[r])
                r -= 1 
                max_r = max(height[r], max_r)

        return res