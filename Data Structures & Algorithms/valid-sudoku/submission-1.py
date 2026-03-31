class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rows = len(board)
        # cols = len(board[0])
        # square = board[]
        rows = len(board)
        cols = len(board[0])
        
        for c in range(cols):
            hash_set = set()
            for r in range(rows):
                if board[r][c] != '.':
                    if board[r][c] in hash_set:
                        return False
                    hash_set.add(board[r][c])
        
        for r in range(rows):
            hash_set = set()
            for c in range(cols):
                if board[r][c] != '.':
                    if board[r][c] in hash_set:
                        return False
                    hash_set.add(board[r][c])

        square = [[set() for _ in range(3)] for _ in range(3)]
        for r in range(rows):
            for c in range(cols):
                if board[r][c] != '.':
                    if board[r][c] in square[r//3][c//3]:
                        return False
                    # (3, 3), (3, 4), (3, 5)
                    # (4, 3), (4, 4), (4, 5)
                    # (5, 3), (5, 4), (5, 5)
                    square[r//3][c//3].add(board[r][c])

        return True
