class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        cols = len(matrix[0])
        rows = len(matrix)
        row_has_zero = any(matrix[0][c] == 0 for c in range(cols))
        col_has_zero = any(matrix[r][0] == 0 for r in range(rows))
        
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0

        for c in range(1, cols):
            if matrix[0][c] == 0:
                for r in range(rows):
                    matrix[r][c] = 0
        for r in range(1, rows):
            if matrix[r][0] == 0:
                for c in range(cols):
                    matrix[r][c] = 0


        if row_has_zero:
            for c in range(cols):
                matrix[0][c] = 0
        
        if col_has_zero:
            for r in range(rows):
                matrix[r][0] = 0
        
        