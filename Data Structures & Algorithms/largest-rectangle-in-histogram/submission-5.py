class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 當遇到右邊有更矮的就結算此區間
        # 補 [0]：虛擬的右邊界，比任何柱子都矮，強制清空 stack

        stack = [] # 存高度遞增的 idx
        max_area = 0

        for i, h in enumerate(heights + [0]):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                left_start = stack[-1] + 1 if stack else 0
                width = i - left_start
                max_area = max(max_area, height*width)
            stack.append(i)
        
        return max_area