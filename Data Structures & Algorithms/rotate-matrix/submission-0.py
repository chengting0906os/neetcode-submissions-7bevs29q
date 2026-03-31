class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix.reverse()
        n = len(matrix)

        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            


"""
1  2  3  4
5  6  7  8
9  10 11 12
13 14 15 16
"""

"""

13 14 15 16
9  10 11 12
5  6  7  8
1  2  3  4
"""


"""
13   9   5   1
14  10   6   2
15  11   7   3
16  12   8   4
"""

