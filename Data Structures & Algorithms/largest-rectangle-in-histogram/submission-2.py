class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # [(leftmost_start, height)]
        max_area = 0

        for i, h in enumerate(heights):
            leftmost_start = i

            while stack and stack[-1][1] > h:
                pre_idx, pre_h = stack.pop()
                max_area = max(max_area, pre_h * (i-pre_idx))
                leftmost_start = pre_idx

            stack.append((leftmost_start, h))
        
        for l_start, h in stack:
            max_area = max(max_area, h * (len(heights) - l_start))
        
        return max_area