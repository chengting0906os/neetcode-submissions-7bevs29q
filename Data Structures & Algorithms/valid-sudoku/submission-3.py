class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # init rows cols
        rows = len(board)
        cols = len(board[0])
        
        # 1, 1    1 // 3
        # 橫排
        row_buckets = [set() for _ in range(9)]
        col_buckets = [set() for _ in range(9)]
        square_buckets = [[set() for _ in range(3)] for _ in range(3)]
        
        for r in range(rows):
            for c in range(cols):
                row_bucket = row_buckets[r]
                col_bucket = col_buckets[c]
                square_bucket = square_buckets[r//3][c//3]
                
                if board[r][c] != ".":
                    if board[r][c] in row_bucket or board[r][c] in col_bucket or board[r][c] in square_bucket:
                        return False
                    else:
                        row_bucket.add(board[r][c])
                        col_bucket.add(board[r][c])
                        square_bucket.add(board[r][c])
        
   
        return True
                
                
                