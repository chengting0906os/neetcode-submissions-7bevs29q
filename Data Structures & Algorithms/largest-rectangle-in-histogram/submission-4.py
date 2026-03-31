class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # 存 index，維持單調遞增
        max_area = 0

        for i, height in enumerate(heights + [0]):  # 補 0 強制清空 stack
            while stack and heights[stack[-1]] >= height:
                popped_height = heights[stack.pop()]
                left_boundary = stack[-1] if stack else -1
                width = i - left_boundary - 1
                max_area = max(max_area, popped_height * width)
            stack.append(i)

        return max_area