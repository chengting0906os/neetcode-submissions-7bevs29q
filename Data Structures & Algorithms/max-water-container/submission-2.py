class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        volumn = 0

        while l < r:
            distance = r - l
            product = min(heights[l], heights[r]) * distance
            if product > volumn:
                volumn = product

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return volumn
