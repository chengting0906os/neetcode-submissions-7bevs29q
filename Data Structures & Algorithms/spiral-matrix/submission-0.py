class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        res = []
        left, right, top, bottom = 0, cols-1, 0, rows-1

        while left <= right and top <= bottom:
            for c in range(left, right + 1):
                res.append(matrix[top][c])

            # right column
            for r in range(top + 1, bottom + 1):
                res.append(matrix[r][right])
            
            if left == right or top == bottom:
                break

            # bottom row
            for c in range(right - 1, left - 1, -1):
                res.append(matrix[bottom][c])

            # left column
            for r in range(bottom - 1, top, -1):
                res.append(matrix[r][left])
            
            left += 1
            right -= 1
            top += 1
            bottom -= 1

        return res
