class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # init rows cols
        rows = len(board)
        cols = len(board[0])
        
        # 1, 1    1 // 3
        # 橫排
        for r in range(rows):
            bucket = set()
            for c in range(cols):
                if board[r][c] != ".":
                    if board[r][c] in bucket:
                        return False
                    else:
                        bucket.add(board[r][c])
        
        # 直排
        for c in range(cols):
            bucket = set()
            for r in range(rows):
                if board[r][c] != ".":
                    if board[r][c] in bucket:
                        return False
                    else:
                        bucket.add(board[r][c])
        
        buckets = [[set() for _ in range(3)] for _ in range(3)]
        
        for r in range(rows):
            for c in range(cols):
                bucket = buckets[r//3][c//3]
                if board[r][c] != ".":
                    if board[r][c] in bucket:
                        return False
                    else:
                        bucket.add(board[r][c])
        
        return True