class NumMatrix:
    """ dp = 
        [0] [0] [0] [0]
        [0] [0] [0] [0]
        [0] [0] [0] [0]
        [0] [0] [0] [0]


    """

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        self.dp = [[0] * (cols + 1) for _ in range(rows + 1)]

        for r in range(rows):
            for c in range(cols):
                self.dp[r+1][c+1] = matrix[r][c] + self.dp[r+1][c] + self.dp[r][c+1] - self.dp[r][c]
                # prefix_fum

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        result = (self.dp[row2+1][col2+1] - self.dp[row1][col2 + 1] - self.dp[row2 + 1][col1] + self.dp[row1][col1])
        return result

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)